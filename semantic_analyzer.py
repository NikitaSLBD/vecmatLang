# semantic_analyzer.py
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple, Any
from antlr4 import *

from generated.vecmatlangLexer import vecmatlangLexer
from generated.vecmatlangParser import vecmatlangParser
from generated.vecmatlangListener import vecmatlangListener

# Типы данных
class Type(Enum):
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    VECTOR = "vector"
    MATRIX = "matrix"
    VOID = "void"
    CLASS = "class"
    STRING = "string"
    UNKNOWN = "unknown"
    
    @staticmethod
    def from_token(token_type: int):
        mapping = {
            45: Type.INT,      # INT_TYPE
            46: Type.FLOAT,    # FLOAT_TYPE
            47: Type.VECTOR,   # VECTOR
            48: Type.MATRIX,   # MATRIX
            52: Type.STRING,   # STRING
        }
        return mapping.get(token_type, Type.UNKNOWN)

class Symbol:
    def __init__(self, name: str, symbol_type: Type, line: int = 0, column: int = 0):
        self.name = name
        self.type = symbol_type
        self.line = line
        self.column = column
        self.is_initialized = False
        
    def __str__(self):
        return f"{self.name}: {self.type.value}"

class FunctionSymbol(Symbol):
    def __init__(self, name: str, return_type: Type, params: List[Type], 
                 line: int = 0, column: int = 0, is_method: bool = False):
        super().__init__(name, return_type, line, column)
        self.params = params  # List of types
        self.is_method = is_method
        self.overloads = []  # Список перегрузок
        
    def add_overload(self, params: List[Type]):
        """Добавить перегрузку функции"""
        self.overloads.append(params)
        
    def find_matching_overload(self, arg_types: List[Type]) -> Optional[List[Type]]:
        """Найти подходящую перегрузку"""
        for overload in self.overloads:
            if len(overload) != len(arg_types):
                continue
                
            match = True
            for expected, actual in zip(overload, arg_types):
                if not self._types_compatible(expected, actual):
                    match = False
                    break
                    
            if match:
                return overload
        return None
        
    def _types_compatible(self, expected: Type, actual: Type) -> bool:
        """Проверка совместимости типов"""
        if expected == Type.UNKNOWN:
            return True
        if expected == actual:
            return True
        # int может быть преобразован в float
        if expected == Type.FLOAT and actual == Type.INT:
            return True
        return False

class ClassSymbol(Symbol):
    def __init__(self, name: str, line: int = 0, column: int = 0):
        super().__init__(name, Type.CLASS, line, column)
        self.fields: Dict[str, Symbol] = {}
        self.methods: Dict[str, FunctionSymbol] = {}
        self.static_funcs: Dict[str, FunctionSymbol] = {}
        
    def add_field(self, name: str, field_type: Type, line: int, column: int):
        self.fields[name] = Symbol(name, field_type, line, column)
        
    def add_method(self, name: str, return_type: Type, params: List[Type], 
                   line: int, column: int):
        self.methods[name] = FunctionSymbol(name, return_type, params, line, column, True)
        
    def add_static_func(self, name: str, return_type: Type, params: List[Type], 
                        line: int, column: int):
        self.static_funcs[name] = FunctionSymbol(name, return_type, params, line, column, False)

class SemanticAnalyzer(vecmatlangListener):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.warnings = []
        
        # Структуры данных для анализа
        self.symbol_table: Dict[str, Symbol] = {}  # Глобальная таблица символов
        self.current_scope: List[Dict[str, Symbol]] = [{}]  # Стек областей видимости
        self.current_class: Optional[ClassSymbol] = None
        self.current_function: Optional[FunctionSymbol] = None
        self.in_class_body = False

        self.in_for_loop = False 
        self.for_loop_vars = []
        
        # Встроенные функции
        self._init_builtins()
        
    def _init_builtins(self):
        """Инициализация встроенных функций"""
        # len() - работает с vector и matrix
        len_func = FunctionSymbol("len", Type.INT, [Type.VECTOR], 0, 0)
        len_func.add_overload([Type.MATRIX])
        self.symbol_table["len"] = len_func
        
        # write() - может принимать любые типы (вариадическая)
        write_func = FunctionSymbol("write", Type.VOID, [], 0, 0)
        self.symbol_table["write"] = write_func
        
        # read() - возвращает строку
        read_func = FunctionSymbol("read", Type.STRING, [], 0, 0)
        self.symbol_table["read"] = read_func
        
        # range() - создает диапазон
        range_func = FunctionSymbol("range", Type.VECTOR, [Type.INT], 0, 0)
        range_func.add_overload([Type.INT, Type.INT])
        range_func.add_overload([Type.INT, Type.INT, Type.INT])
        self.symbol_table["range"] = range_func
        
    def _add_error(self, message: str, line: int = 0, column: int = 0):
        self.errors.append(f"Ошибка в строке {line}, колонке {column}: {message}")
        
    def _add_warning(self, message: str, line: int = 0, column: int = 0):
        self.warnings.append(f"Предупреждение в строке {line}, колонке {column}: {message}")
        
    def _enter_scope(self):
        self.current_scope.append({})
        
    def _exit_scope(self):
        if len(self.current_scope) > 1:
            self.current_scope.pop()
            
    def _lookup_symbol(self, name: str) -> Optional[Symbol]:
        """Поиск символа в текущих областях видимости"""
        for scope in reversed(self.current_scope):
            if name in scope:
                return scope[name]
        return self.symbol_table.get(name)
        
    def _current_scope_table(self) -> Dict[str, Symbol]:
        return self.current_scope[-1]
        
    # ========== Обработка объявлений ==========
    
    def enterFunctionDecl(self, ctx: vecmatlangParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        line = ctx.start.line
        column = ctx.start.column
        
        # Определяем тип возвращаемого значения
        return_type = Type.UNKNOWN
        
        # Парсим параметры
        params = []
        param_list = ctx.parameterList()
        if param_list:
            # В динамически типизированном языке параметры имеют тип UNKNOWN
            params = [Type.UNKNOWN] * len(param_list.ID())
        
        # Ищем существующую функцию
        existing_symbol = self._lookup_symbol(func_name)
        func_sym = None  # Инициализируем переменную
        
        if existing_symbol:
            if isinstance(existing_symbol, FunctionSymbol):
                # Добавляем перегрузку к существующей функции
                existing_symbol.add_overload(params)
                self._add_warning(f"Перегрузка функции '{func_name}'", line, column)
                func_sym = existing_symbol  # Используем существующий символ
            else:
                self._add_error(f"Имя '{func_name}' уже используется для другой сущности", line, column)
                return  # Выходим, не устанавливая current_function
        else:
            # Создаем новую функцию
            func_sym = FunctionSymbol(func_name, return_type, params, line, column)
            self.symbol_table[func_name] = func_sym
        
        # Устанавливаем текущую функцию только если func_sym был создан
        if func_sym:
            self.current_function = func_sym
            self._enter_scope()
            
            # Добавляем параметры в область видимости как ИНИЦИАЛИЗИРОВАННЫЕ
            if param_list:
                for param in param_list.ID():
                    param_name = param.getText()
                    param_symbol = Symbol(param_name, Type.UNKNOWN, 
                                        param.symbol.line, param.symbol.column)
                    param_symbol.is_initialized = True
                    self._current_scope_table()[param_name] = param_symbol
        else:
            # Не должно происходить, но на всякий случай
            self._add_error(f"Не удалось создать символ функции '{func_name}'", line, column)
                
    def exitFunctionDecl(self, ctx: vecmatlangParser.FunctionDeclContext):
        self.current_function = None
        self._exit_scope()
        
    def enterClassDecl(self, ctx: vecmatlangParser.ClassDeclContext):
        class_name = ctx.ID().getText()
        line = ctx.start.line
        column = ctx.start.column
        
        # Проверяем, не объявлен ли уже класс
        if class_name in self.symbol_table:
            self._add_error(f"Класс '{class_name}' уже объявлен", line, column)
            return
            
        # Создаем символ класса
        class_sym = ClassSymbol(class_name, line, column)
        self.symbol_table[class_name] = class_sym
        self.current_class = class_sym
        self.in_class_body = True
        
        # Добавляем параметры конструктора в область видимости
        self._enter_scope()
        param_list = ctx.parameterList()
        if param_list:
            for param in param_list.ID():
                param_name = param.getText()
                self._current_scope_table()[param_name] = Symbol(param_name, Type.UNKNOWN,
                                                                param.symbol.line, param.symbol.column)
                
    def exitClassDecl(self, ctx: vecmatlangParser.ClassDeclContext):
        self.current_class = None
        self.in_class_body = False
        self._exit_scope()
        
    def enterMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        if not self.current_class:
            self._add_error("Метод объявлен вне класса", ctx.start.line, ctx.start.column)
            return
            
        method_name = ctx.ID().getText()
        line = ctx.start.line
        column = ctx.start.column
        
        # Определяем, это метод или статическая функция (в грамматике нет различия,
        # будем считать все методы нестатическими)
        return_type = Type.VOID
        
        # Парсим параметры
        params = []
        param_list = ctx.parameterList()
        if param_list:
            params = [Type.UNKNOWN] * len(param_list.ID())
            
        # Добавляем метод в класс
        self.current_class.add_method(method_name, return_type, params, line, column)
        
        # Входим в область видимости метода
        self._enter_scope()
        
        # Неявный параметр self для методов
        self._current_scope_table()["self"] = Symbol("self", Type.CLASS, line, column)
        
        # Добавляем параметры метода
        if param_list:
            for param in param_list.ID():
                param_name = param.getText()
                self._current_scope_table()[param_name] = Symbol(param_name, Type.UNKNOWN,
                                                                param.symbol.line, param.symbol.column)
                
    def exitMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        self._exit_scope()
        
    # ========== Обработка присваиваний ==========
    
    def enterSingleAssignment(self, ctx: vecmatlangParser.SingleAssignmentContext):

        var_ctx = ctx.var()
        expr_ctx = ctx.expression()
        
        # Определяем имя переменной
        var_name = self._get_var_name(var_ctx)
        if not var_name:
            return
            
        # Анализируем тип выражения
        expr_type = self._analyze_expression(expr_ctx)
        
        # Если это простое имя переменной (не поле класса)
        if ctx.var().ID():
            # Проверяем, объявлена ли уже переменная
            existing_symbol = self._lookup_symbol(var_name)
            
            if not existing_symbol:
                # Если не объявлена - добавляем в текущую область видимости
                new_symbol = Symbol(var_name, expr_type, ctx.start.line, ctx.start.column)
                new_symbol.is_initialized = True
                self._current_scope_table()[var_name] = new_symbol
            else:
                # Если объявлена - проверяем совместимость типов
                if existing_symbol.type != Type.UNKNOWN and existing_symbol.type != expr_type:
                    # Проверяем числовое преобразование
                    if not (existing_symbol.type == Type.FLOAT and expr_type == Type.INT):
                        self._add_error(f"Тип {expr_type.value} несовместим с типом переменной {existing_symbol.type.value}",
                                      ctx.start.line, ctx.start.column)
                existing_symbol.is_initialized = True
                
        # Если это обращение к полю класса (obj.field)
        elif ctx.var().fieldAppeal():
            # Проверяем, что поле существует и доступно для записи
            field_name_parts = var_name.split('.')
            if len(field_name_parts) == 2:
                obj_name, field_name = field_name_parts
                
                # Находим объект
                obj_symbol = self._lookup_symbol(obj_name)
                if not obj_symbol or obj_symbol.type != Type.CLASS:
                    self._add_error(f"Объект '{obj_name}' не найден",
                                  var_ctx.start.line, var_ctx.start.column)
                    return
                    
                # Находим класс
                class_sym = self.symbol_table.get(obj_name)
                if not isinstance(class_sym, ClassSymbol):
                    self._add_error(f"'{obj_name}' не является классом",
                                  var_ctx.start.line, var_ctx.start.column)
                    return
                    
                # Проверяем, что поле существует
                field = class_sym.fields.get(field_name)
                if not field:
                    self._add_error(f"Поле '{field_name}' не найдено в классе '{obj_name}'",
                                  var_ctx.start.line, var_ctx.start.column)
                    return
                    
                # Проверяем совместимость типов
                if field.type != expr_type and not (field.type == Type.FLOAT and expr_type == Type.INT):
                    self._add_error(f"Тип {expr_type.value} несовместим с типом поля {field.type.value}",
                                  var_ctx.start.line, var_ctx.start.column)
        else:
            # Для индексированных переменных пока пропускаем проверку
            pass
                
    def enterMultipleAssignment(self, ctx: vecmatlangParser.MultipleAssignmentContext):
        """Обработка множественного присваивания: x, y = swap(x, y)"""
        
        # Получаем переменные слева
        var_nodes = []
        if hasattr(ctx, 'var') and ctx.var():
            var_nodes = ctx.var()
            
        # Получаем выражение справа (может быть primaryExpression или список выражений)
        if hasattr(ctx, 'primaryExpression'):
            # Случай: x, y = swap(x, y)
            expr = ctx.primaryExpression()
            expr_type = self._analyze_primary_expression(expr)
            
            # Если это вызов функции swap, проверяем количество аргументов
            if isinstance(expr, vecmatlangParser.FuncCallExprContext):
                func_name = expr.ID().getText()
                func_symbol = self._lookup_symbol(func_name)
                
                if isinstance(func_symbol, FunctionSymbol):
                    # Проверяем количество возвращаемых значений
                    arg_list = expr.argumentList()
                    if arg_list:
                        # Для swap количество возвращаемых значений = количеству аргументов
                        expected_returns = len(arg_list.expression())
                        actual_vars = len(var_nodes) if hasattr(var_nodes, '__len__') else 1
                        
                        if expected_returns != actual_vars:
                            self._add_error(f"Функция '{func_name}' возвращает {expected_returns} значений, но присваивается {actual_vars} переменным",
                                        ctx.start.line, ctx.start.column)
                            
        elif hasattr(ctx, 'expression') and ctx.expression():
            # Случай: a, b, c = b, c, a (прямое присваивание)
            expr_nodes = ctx.expression()
            var_count = len(var_nodes) if hasattr(var_nodes, '__len__') else 0
            expr_count = len(expr_nodes) if hasattr(expr_nodes, '__len__') else 0
            
            if var_count != expr_count:
                self._add_error(f"Количество переменных ({var_count}) не совпадает с количеством выражений ({expr_count})",
                            ctx.start.line, ctx.start.column)
                
            # Анализируем все выражения
            for expr in expr_nodes:
                self._analyze_expression(expr)
                
        # Добавляем/обновляем переменные
        if hasattr(ctx, 'var') and ctx.var():
            for var_node in var_nodes:
                if var_node.ID():
                    var_name = var_node.ID().getText()
                    existing_symbol = self._lookup_symbol(var_name)
                    
                    if not existing_symbol:
                        # Создаем новую переменную с типом UNKNOWN
                        new_symbol = Symbol(var_name, Type.UNKNOWN, var_node.start.line, var_node.start.column)
                        new_symbol.is_initialized = True
                        self._current_scope_table()[var_name] = new_symbol
                    else:
                        existing_symbol.is_initialized = True

    def _get_var_name(self, var_ctx) -> Optional[str]:
        """Извлекает имя переменной из узла var"""
        if var_ctx.ID():
            return var_ctx.ID().getText()
        elif var_ctx.fieldAppeal():
            field_appeal = var_ctx.fieldAppeal()
            return f"{field_appeal.ID(0).getText()}.{field_appeal.ID(1).getText()}"
        return None
        
    # ========== Анализ выражений ==========
    
    def _analyze_expression(self, expr_ctx) -> Type:
        """Анализирует выражение и возвращает его тип"""
        if isinstance(expr_ctx, vecmatlangParser.PrimaryExprContext):
            return self._analyze_primary_expression(expr_ctx.primaryExpression())
        elif isinstance(expr_ctx, vecmatlangParser.NormExprContext):
            # Норма вектора/матрицы: |expr|
            inner_type = self._analyze_expression(expr_ctx.expression())
            if inner_type not in [Type.VECTOR, Type.MATRIX]:
                self._add_error("Оператор '||' применяется только к vector и matrix", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
            return Type.FLOAT
        elif isinstance(expr_ctx, vecmatlangParser.UnaryMinusExprContext):
            inner_type = self._analyze_expression(expr_ctx.expression())
            if inner_type not in [Type.INT, Type.FLOAT, Type.VECTOR, Type.MATRIX]:
                self._add_error("Унарный минус применяется только к числам, векторам и матрицам", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
            return inner_type
        elif isinstance(expr_ctx, vecmatlangParser.IndexExprContext):
            # Индексация: expr[expr]
            obj_type = self._analyze_expression(expr_ctx.expression(0))
            index_type = self._analyze_expression(expr_ctx.expression(1))
            
            if index_type != Type.INT:
                self._add_error(f"Индекс должен быть int, получен {index_type.value}", 
                              expr_ctx.start.line, expr_ctx.start.column)
                
            if obj_type == Type.VECTOR:
                return Type.FLOAT
            elif obj_type == Type.MATRIX:
                return Type.VECTOR
            else:
                self._add_error("Индексация применяется только к vector и matrix", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
        elif isinstance(expr_ctx, (vecmatlangParser.MulDivExprContext, 
                                  vecmatlangParser.AddSubExprContext,
                                  vecmatlangParser.ComparisonExprContext,
                                  vecmatlangParser.BinlogicExprContext)):
            return self._analyze_binary_op(expr_ctx)
        elif isinstance(expr_ctx, vecmatlangParser.NotExprContext):
            inner_type = self._analyze_expression(expr_ctx.expression())
            if inner_type != Type.BOOL:
                self._add_error("Оператор '!' применяется только к bool", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
            return Type.BOOL
            
        return Type.UNKNOWN
        
    def _analyze_binary_op(self, expr_ctx) -> Type:
        """Анализ бинарной операции"""
        left_type = self._analyze_expression(expr_ctx.expression(0))
        right_type = self._analyze_expression(expr_ctx.expression(1))
        
        # Определяем оператор
        if isinstance(expr_ctx, vecmatlangParser.MulDivExprContext):
            op_text = expr_ctx.getChild(1).getText()
            return self._get_mul_div_result_type(left_type, right_type, op_text, 
                                                expr_ctx.start.line, expr_ctx.start.column)
        elif isinstance(expr_ctx, vecmatlangParser.AddSubExprContext):
            op_text = expr_ctx.getChild(1).getText()
            return self._get_add_sub_result_type(left_type, right_type, op_text,
                                                expr_ctx.start.line, expr_ctx.start.column)
        elif isinstance(expr_ctx, vecmatlangParser.ComparisonExprContext):
            # Сравнение всегда возвращает bool
            if not self._are_types_comparable(left_type, right_type):
                self._add_error(f"Нельзя сравнивать {left_type.value} и {right_type.value}", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
            return Type.BOOL
        elif isinstance(expr_ctx, vecmatlangParser.BinlogicExprContext):
            # Логические операции требуют bool
            if left_type != Type.BOOL or right_type != Type.BOOL:
                self._add_error("Логические операции применяются только к bool", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
            return Type.BOOL
            
        return Type.UNKNOWN
        
    def _analyze_primary_expression(self, primary_ctx) -> Type:
        """Анализ первичного выражения"""
        if isinstance(primary_ctx, vecmatlangParser.IdExprContext):
            # Идентификатор или переменная
            if primary_ctx.ID():
                var_name = primary_ctx.ID().getText()
                symbol = self._lookup_symbol(var_name)
                
                if not symbol:
                    # Если переменная не найдена, создаем с типом UNKNOWN
                    symbol = Symbol(var_name, Type.UNKNOWN, primary_ctx.start.line, primary_ctx.start.column)
                    self._current_scope_table()[var_name] = symbol
                    return Type.UNKNOWN
                    
                # СПЕЦИАЛЬНАЯ ПРОВЕРКА: если переменная - это переменная цикла for,
                # то она считается инициализированной
                if var_name in self.for_loop_vars:
                    return symbol.type
                    
                # В ДИНАМИЧЕСКОЙ ТИПИЗАЦИИ: параметры функций всегда инициализированы
                # Нужно проверить, является ли это параметром текущей функции
                if (self.current_function and 
                    any(param_name == var_name for param_name in self._current_scope_table().keys())):
                    # Это параметр функции, считаем инициализированным
                    return symbol.type
                    
                if not symbol.is_initialized:
                    self._add_warning(f"Переменная '{var_name}' используется до инициализации",
                                    primary_ctx.start.line, primary_ctx.start.column)
                    
                return symbol.type
                
            elif primary_ctx.var():
                # Это уже проанализированная переменная
                var_ctx = primary_ctx.var()
                if var_ctx.ID():
                    var_name = var_ctx.ID().getText()
                    symbol = self._lookup_symbol(var_name)
                    
                    # СПЕЦИАЛЬНАЯ ПРОВЕРКА для переменных цикла
                    if var_name in self.for_loop_vars:
                        return symbol.type if symbol else Type.INT
                    
                    return symbol.type if symbol else Type.UNKNOWN
                else:
                    return Type.UNKNOWN
                
        elif isinstance(primary_ctx, vecmatlangParser.ParenExprContext):
            return self._analyze_expression(primary_ctx.expression())
            
        elif isinstance(primary_ctx, vecmatlangParser.FuncCallExprContext):
            return self._analyze_function_call(primary_ctx)
            
        elif isinstance(primary_ctx, vecmatlangParser.FieldExprContext):
            # Обращение к полю класса
            field_ctx = primary_ctx.fieldAppeal()
            obj_name = field_ctx.ID(0).getText()
            field_name = field_ctx.ID(1).getText()
            
            # Проверяем, что объект существует
            obj_symbol = self._lookup_symbol(obj_name)
            if not obj_symbol or obj_symbol.type != Type.CLASS:
                self._add_error(f"Объект '{obj_name}' не найден или не является классом", 
                              field_ctx.start.line, field_ctx.start.column)
                return Type.UNKNOWN
                
            # Получаем класс
            class_sym = self.symbol_table.get(obj_name)
            if not isinstance(class_sym, ClassSymbol):
                self._add_error(f"'{obj_name}' не является классом", 
                              field_ctx.start.line, field_ctx.start.column)
                return Type.UNKNOWN
                
            # Проверяем поле
            field = class_sym.fields.get(field_name)
            if not field:
                self._add_error(f"Поле '{field_name}' не найдено в классе '{obj_name}'", 
                              field_ctx.start.line, field_ctx.start.column)
                return Type.UNKNOWN
                
            return field.type
            
        elif isinstance(primary_ctx, vecmatlangParser.MethodExprContext):
            # Вызов метода класса
            method_ctx = primary_ctx.methodAppeal()
            obj_name = method_ctx.ID(0).getText()
            method_name = method_ctx.ID(1).getText()
            
            # Проверяем объект
            obj_symbol = self._lookup_symbol(obj_name)
            if not obj_symbol or obj_symbol.type != Type.CLASS:
                self._add_error(f"Объект '{obj_name}' не найден", 
                              method_ctx.start.line, method_ctx.start.column)
                return Type.UNKNOWN
                
            # Получаем класс
            class_sym = self.symbol_table.get(obj_name)
            if not isinstance(class_sym, ClassSymbol):
                self._add_error(f"'{obj_name}' не является классом", 
                              method_ctx.start.line, method_ctx.start.column)
                return Type.UNKNOWN
                
            # Проверяем метод
            method = class_sym.methods.get(method_name)
            if not method:
                self._add_error(f"Метод '{method_name}' не найден в классе '{obj_name}'", 
                              method_ctx.start.line, method_ctx.start.column)
                return Type.UNKNOWN
                
            # Проверяем аргументы
            arg_list = method_ctx.argumentList()
            if arg_list:
                arg_types = []
                for expr in arg_list.expression():
                    arg_types.append(self._analyze_expression(expr))
                    
                # Ищем подходящую перегрузку
                if not method.find_matching_overload(arg_types):
                    self._add_error(f"Не найдена подходящая перегрузка метода '{method_name}'", 
                                  method_ctx.start.line, method_ctx.start.column)
                    
            return method.type
            
        elif isinstance(primary_ctx, vecmatlangParser.LiteralExprContext):
            return self._analyze_literal(primary_ctx.literal())
            
        elif isinstance(primary_ctx, vecmatlangParser.TypeExprContext):
            # Конструктор типа: int(5), vector([1,2,3])
            type_ctx = primary_ctx.type_()
            type_token = type_ctx.start.type
            target_type = Type.from_token(type_token)
            
            # Проверяем аргументы конструктора
            arg_list = primary_ctx.argumentList()
            if arg_list:
                for expr in arg_list.expression():
                    expr_type = self._analyze_expression(expr)
                    # Базовая проверка типов
                    if target_type == Type.VECTOR and expr_type not in [Type.INT, Type.FLOAT]:
                        self._add_error(f"Вектор может содержать только числа", 
                                      primary_ctx.start.line, primary_ctx.start.column)
                        
            return target_type
            
        elif isinstance(primary_ctx, vecmatlangParser.LenExprContext):
            # len() функция
            arg_list = primary_ctx.argumentList()
            if not arg_list or len(arg_list.expression()) != 1:
                self._add_error("Функция len() принимает ровно один аргумент", 
                              primary_ctx.start.line, primary_ctx.start.column)
                return Type.UNKNOWN
                
            arg_type = self._analyze_expression(arg_list.expression(0))
            if arg_type not in [Type.VECTOR, Type.MATRIX]:
                self._add_error("Функция len() применяется только к vector и matrix", 
                              primary_ctx.start.line, primary_ctx.start.column)
                return Type.UNKNOWN
                
            return Type.INT
            
        elif isinstance(primary_ctx, vecmatlangParser.ReadExprContext):
            return Type.STRING
            
        return Type.UNKNOWN
        
    def _analyze_function_call(self, func_ctx) -> Type:
        """Анализ вызова функции"""
        func_name = func_ctx.ID().getText()
        line = func_ctx.start.line
        column = func_ctx.start.column
        
        # Ищем функцию
        func_symbol = self._lookup_symbol(func_name)
        if not func_symbol or not isinstance(func_symbol, FunctionSymbol):
            self._add_error(f"Функция '{func_name}' не объявлена", line, column)
            return Type.UNKNOWN
            
        # Анализируем аргументы
        arg_types = []
        arg_list = func_ctx.argumentList()
        if arg_list:
            for expr in arg_list.expression():
                arg_types.append(self._analyze_expression(expr))
        
        # Для функций с перегрузками пытаемся найти подходящую
        if func_symbol.overloads:
            # Ищем перегрузку с подходящим количеством аргументов
            matching_overload = None
            for overload in func_symbol.overloads:
                if len(overload) == len(arg_types):
                    matching_overload = overload
                    break
                    
            if not matching_overload:
                self._add_error(f"Не найдена подходящая перегрузка функции '{func_name}' с {len(arg_types)} аргументами", 
                            line, column)
        else:
            # Для функций без перегрузок проверяем количество параметров
            if len(arg_types) != len(func_symbol.params):
                self._add_error(f"Функция '{func_name}' ожидает {len(func_symbol.params)} аргументов, получено {len(arg_types)}", 
                            line, column)
        
        # Обработка встроенных функций
        if func_name in ["range", "int", "float", "write", "read"]:
            # ... обработка как раньше ...
            pass
            
        # Для пользовательских функций в динамически типизированном языке
        # возвращаем UNKNOWN (функция может вернуть любое значение)
        return Type.UNKNOWN
        
    def _analyze_literal(self, literal_ctx) -> Type:
        """Анализ литерала"""

        print(f"Начинаю анализ литерала: {literal_ctx.getText()[:20]}...")
        
        if isinstance(literal_ctx, vecmatlangParser.IntLiteralContext):
            print(f"  Это int литерал: {literal_ctx.getText()}")
            return Type.INT
        elif isinstance(literal_ctx, vecmatlangParser.FloatLiteralContext):
            print(f"  Это float литерал: {literal_ctx.getText()}")
            return Type.FLOAT
        elif isinstance(literal_ctx, vecmatlangParser.StringLiteralContext):
            print(f"  Это string литерал: {literal_ctx.getText()}")
            return Type.STRING
        elif isinstance(literal_ctx, vecmatlangParser.VectorLiteralContext):
            print(f"Начинаю анализ вектора {literal_ctx.getText()}")
            return self._analyze_vector_literal(literal_ctx)
        elif isinstance(literal_ctx, vecmatlangParser.MatrixLiteralContext):
            print(f"Начинаю анализ матрицы {literal_ctx.getText()}")
            return self._analyze_matrix_literal(literal_ctx)
        
        print(f"  Неизвестный тип литерала: {type(literal_ctx).__name__}")
        return Type.UNKNOWN

    def _analyze_vector_literal(self, vector_ctx) -> Type:
        """Анализ векторного литерала"""
        print(f"  Анализ векторного литерала: {vector_ctx.getText()}")
        
        # Проверяем, не является ли это на самом деле матрицей
        text = vector_ctx.getText()
        if text.startswith('[[') and text.endswith(']]'):
            # Это может быть матрица, проанализированная как вектор
            print(f"  Внимание: векторный литерал выглядит как матрица: {text}")
            
            # Попробуем проанализировать как матрицу
            # Для этого нужно проверить элементы
            if vector_ctx.expression():
                for expr in vector_ctx.expression():
                    expr_text = expr.getText() if hasattr(expr, 'getText') else str(expr)
                    print(f"  Элемент вектора: {expr_text}")
                    
                    # Если элемент сам является векторным литералом, это матрица
                    if isinstance(expr, vecmatlangParser.VectorLiteralContext):
                        print(f"  Элемент - вектор, значит это матрица!")
                        return Type.MATRIX
                        
            print(f"  Элементы не являются векторами, оставляем как вектор")
        
        # Обычный анализ вектора
        if not vector_ctx.expression():
            return Type.VECTOR  # Пустой вектор
        
        elem_types = []
        for expr in vector_ctx.expression():
            elem_type = self._analyze_expression(expr)
            print(f"  Тип элемента вектора: {elem_type.value}")
            
            if elem_type not in [Type.INT, Type.FLOAT, Type.VECTOR, Type.MATRIX]:
                self._add_error(f"Векторный элемент должен быть числом или вектором, получен {elem_type.value}", 
                            expr.start.line, expr.start.column)
                return Type.VECTOR
            elem_types.append(elem_type)
        
        # Определяем тип: если хотя бы один элемент - вектор, это матрица
        if any(t == Type.VECTOR for t in elem_types):
            print(f"  Вектор содержит векторы -> это матрица")
            
            # Проверяем, что все элементы - векторы одинаковой длины
            vector_lengths = []
            for expr in vector_ctx.expression():
                if isinstance(expr, vecmatlangParser.VectorLiteralContext):
                    vector_lengths.append(len(expr.expression()))
            
            if vector_lengths:
                first_len = vector_lengths[0]
                for i, length in enumerate(vector_lengths[1:], 1):
                    if length != first_len:
                        self._add_error(f"Строки матрицы имеют разную длину: строка {i+1} имеет {length} элементов, строка 1 имеет {first_len}", 
                                    expr.start.line, expr.start.column)
            
            return Type.MATRIX
        elif any(t == Type.MATRIX for t in elem_types):
            print(f"  Вектор содержит матрицы -> это тензор 3D (пока не поддерживается)")
            self._add_warning("Тензоры 3D и выше не поддерживаются", 
                            vector_ctx.start.line, vector_ctx.start.column)
            return Type.MATRIX  # Возвращаем как матрицу для совместимости
        
        # Определяем тип вектора на основе элементов
        if Type.FLOAT in elem_types:
            return Type.VECTOR  # вектор с float элементами
        return Type.VECTOR  # вектор с int элементами

    def _analyze_matrix_literal(self, matrix_ctx) -> Type:
        """Анализ матричного литерала"""
        print(f"  Анализ матричного литерала (настоящего): {matrix_ctx.getText()}")
        
        # Матричный литерал в грамматике: '[' '[' expr (',' expr)* ']' (',' '[' expr (',' expr)* ']')* ']'
        # Нужно получить все строки матрицы
        
        # Собираем строки матрицы
        rows = []
        
        # Обходим детей контекста, ищем векторные литералы
        for i in range(matrix_ctx.getChildCount()):
            child = matrix_ctx.getChild(i)
            print(f"  Дочерний элемент {i}: {type(child).__name__} - {child.getText()[:20] if hasattr(child, 'getText') else 'N/A'}")
            
            if isinstance(child, vecmatlangParser.VectorLiteralContext):
                print(f"  Найден векторный литерал как строка матрицы")
                rows.append(child)
            elif isinstance(child, vecmatlangParser.ExpressionContext):
                # Может быть выражение внутри
                pass
        
        # Если не нашли строки через векторные литералы, используем альтернативный подход
        if not rows:
            print(f"  Не найдены строки матрицы стандартным способом, используем альтернативный")
            # Пробуем найти строки через текст
            text = matrix_ctx.getText()
            
            # Удаляем внешние скобки
            if text.startswith('[[') and text.endswith(']]'):
                inner = text[2:-2]
                # Разделяем строки по '],[' или '], ['
                row_texts = []
                if '],[' in inner:
                    row_texts = inner.split('],[')
                elif '], [' in inner:
                    row_texts = inner.split('], [')
                else:
                    row_texts = [inner]
                
                print(f"  Найдено строк через текстовый анализ: {len(row_texts)}")
        
        # Проверяем строки
        if rows:
            row_lengths = []
            elem_types = set()
            
            for i, row_ctx in enumerate(rows):
                if not row_ctx.expression():
                    self._add_error(f"Строка матрицы {i+1} пустая", 
                                row_ctx.start.line, row_ctx.start.column)
                    continue
                    
                row_lengths.append(len(row_ctx.expression()))
                
                for expr in row_ctx.expression():
                    elem_type = self._analyze_expression(expr)
                    if elem_type not in [Type.INT, Type.FLOAT]:
                        self._add_error(f"Элемент матрицы должен быть числом, получен {elem_type.value}", 
                                    expr.start.line, expr.start.column)
                    elem_types.add(elem_type)
            
            # Проверяем одинаковую длину строк
            if row_lengths:
                first_length = row_lengths[0]
                for i, length in enumerate(row_lengths[1:], 1):
                    if length != first_length:
                        self._add_error(f"Строка {i+1} имеет длину {length}, а должна быть {first_length}", 
                                    rows[i].start.line, rows[i].start.column)
                        break
            
            print(f"  Матрица успешно проанализирована: {len(rows)} строк, {first_length if row_lengths else 0} столбцов")
        
        return Type.MATRIX
        
    # ========== Проверки совместимости типов ==========
    
    def _get_mul_div_result_type(self, left: Type, right: Type, op: str, line: int, col: int) -> Type:
        """Определяет тип результата для операций * и / (для динамической типизации)"""
        # В ДИНАМИЧЕСКОЙ ТИПИЗАЦИИ: разрешаем больше комбинаций
        
        # Если любой из типов UNKNOWN, результат UNKNOWN
        if left == Type.UNKNOWN or right == Type.UNKNOWN:
            return Type.UNKNOWN
            
        # Числовые операции
        if left in [Type.INT, Type.FLOAT] and right in [Type.INT, Type.FLOAT]:
            if left == Type.FLOAT or right == Type.FLOAT:
                return Type.FLOAT
            return Type.INT
            
        # Векторные операции
        elif left == Type.VECTOR and right == Type.VECTOR:
            if op == '*':  # Скалярное произведение
                return Type.FLOAT
            elif op == '/':
                self._add_error("Векторы нельзя делить", line, col)
                return Type.UNKNOWN
            else:
                self._add_error(f"Операция '{op}' не поддерживается для векторов", line, col)
                return Type.UNKNOWN
                
        # Вектор и число
        elif left == Type.VECTOR and right in [Type.INT, Type.FLOAT]:
            if op in ['*', '/']:
                return Type.VECTOR
            else:
                self._add_error(f"Операция '{op}' не поддерживается между vector и числом", line, col)
                return Type.UNKNOWN
                
        elif left in [Type.INT, Type.FLOAT] and right == Type.VECTOR:
            if op == '*':
                return Type.VECTOR
            elif op == '/':
                self._add_error("Число нельзя делить на вектор", line, col)
                return Type.UNKNOWN
            else:
                self._add_error(f"Операция '{op}' не поддерживается между числом и vector", line, col)
                return Type.UNKNOWN
                
        # Матричные операции (упрощенно)
        elif left == Type.MATRIX and right == Type.MATRIX:
            if op in ['+', '-']:
                return Type.MATRIX
            elif op == '*':
                return Type.MATRIX
            else:
                self._add_error(f"Операция '{op}' не поддерживается для матриц", line, col)
                return Type.UNKNOWN
                
        elif left == Type.MATRIX and right in [Type.INT, Type.FLOAT]:
            if op in ['*', '/']:
                return Type.MATRIX
            else:
                self._add_error(f"Операция '{op}' не поддерживается между matrix и числом", line, col)
                return Type.UNKNOWN
                
        elif left == Type.MATRIX and right == Type.VECTOR:
            if op == '*':
                return Type.VECTOR  # Умножение матрицы на вектор
            else:
                self._add_error(f"Операция '{op}' не поддерживается между matrix и vector", line, col)
                return Type.UNKNOWN
                
        if left != right and left != Type.UNKNOWN and right != Type.UNKNOWN:
            self._add_warning(f"Возможная несовместимость типов для операции '{op}': {left.value} и {right.value}", 
                           line, col)
            return Type.UNKNOWN
            
        return Type.UNKNOWN
        
    def _get_add_sub_result_type(self, left: Type, right: Type, op: str, line: int, col: int) -> Type:
        """Определяет тип результата для операций + и -"""
        # Числовые операции
        if left in [Type.INT, Type.FLOAT] and right in [Type.INT, Type.FLOAT]:
            if left == Type.FLOAT or right == Type.FLOAT:
                return Type.FLOAT
            return Type.INT
            
        # Векторные операции
        elif left == Type.VECTOR and right == Type.VECTOR:
            return Type.VECTOR
            
        # Вектор и число (только + и - с особыми правилами)
        elif left == Type.VECTOR and right in [Type.INT, Type.FLOAT]:
            return Type.VECTOR
            
        elif left in [Type.INT, Type.FLOAT] and right == Type.VECTOR:
            return Type.VECTOR
            
        # Матричные операции
        elif left == Type.MATRIX and right == Type.MATRIX:
            return Type.MATRIX
            
        elif left == Type.MATRIX and right in [Type.INT, Type.FLOAT]:
            return Type.MATRIX
            
        self._add_error(f"Несовместимые типы для операции '{op}': {left.value} и {right.value}", 
                       line, col)
        return Type.UNKNOWN
        
    def _are_types_comparable(self, left: Type, right: Type) -> bool:
        """Можно ли сравнивать типы"""
        # Числа можно сравнивать с числами
        if left in [Type.INT, Type.FLOAT] and right in [Type.INT, Type.FLOAT]:
            return True
        # Векторы/матрицы можно сравнивать только с такими же
        if left in [Type.VECTOR, Type.MATRIX] and left == right:
            return True
        # Bool можно сравнивать с bool
        if left == Type.BOOL and right == Type.BOOL:
            return True
        # Строки можно сравнивать со строками
        if left == Type.STRING and right == Type.STRING:
            return True
        return False
        
    # ========== Обработка переменных ==========
    
    def enterVar(self, ctx: vecmatlangParser.VarContext):
        """Обработка использования переменной (например, в индексации)"""
        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self._lookup_symbol(var_name)
            
            if not symbol:
                # Создаем символ с типом UNKNOWN, если переменная используется до объявления
                # (например, в индексации: a[i] где i еще не объявлен)
                symbol = Symbol(var_name, Type.UNKNOWN, ctx.start.line, ctx.start.column)
                self._current_scope_table()[var_name] = symbol
            elif not symbol.is_initialized:
                self._add_warning(f"Переменная '{var_name}' используется до инициализации",
                                ctx.start.line, ctx.start.column)
                    
    # ========== Дополнительные проверки ==========
    

    def enterReturnStatement(self, ctx: vecmatlangParser.ReturnStatementContext):
        if not self.current_function:
            self._add_error("Оператор return вне функции", ctx.start.line, ctx.start.column)
            return
            
        # Проверяем аргументы return
        arg_list = ctx.argumentList()
        if arg_list:
            # Анализируем все возвращаемые выражения
            for expr in arg_list.expression():
                self._analyze_expression(expr)
                
            # Если возвращается несколько значений, устанавливаем специальный тип
            if len(arg_list.expression()) > 1:
                # В динамической типизации можно возвращать кортеж значений
                # Устанавливаем тип как UNKNOWN или создаем специальный тип TUPLE
                return Type.UNKNOWN
                
        else:
            # return без аргументов - возвращает None/void
            return Type.VOID
            
    def enterForStatement(self, ctx: vecmatlangParser.ForStatementContext):
        """Вход в for statement"""
        self.in_for_loop = True
        
        # Получаем имя переменной цикла
        var_name = ctx.ID().getText()
        
        # Добавляем переменную цикла в специальный список
        self.for_loop_vars.append(var_name)
        
        # Добавляем переменную цикла в область видимости как int
        self._current_scope_table()[var_name] = Symbol(var_name, Type.INT, 
                                                      ctx.start.line, ctx.start.column)
        # Отмечаем как инициализированную
        self._current_scope_table()[var_name].is_initialized = True
        
        # Проверяем, что используется range()
        if not ctx.RANGE():
            self._add_error("Цикл for должен использовать функцию range()", 
                           ctx.start.line, ctx.start.column)
            return
            
        # В ДИНАМИЧЕСКОЙ ТИПИЗАЦИИ: не проверяем типы аргументов range строго
        # Проверяем только количество аргументов
        if ctx.expression():
            args = ctx.expression()
            if len(args) < 1 or len(args) > 3:
                self._add_error("Функция range() принимает от 1 до 3 аргументов", 
                              ctx.start.line, ctx.start.column)
                    
    def exitForStatement(self, ctx: vecmatlangParser.ForStatementContext):
        """Выход из for statement"""
        self.in_for_loop = False
        if self.for_loop_vars:
            var_name = self.for_loop_vars.pop()

# ========== Утилита для запуска анализа ==========

def analyze_code(code: str) -> Tuple[List[str], List[str]]:
    """Анализирует код и возвращает ошибки и предупреждения"""
    from antlr4 import InputStream, CommonTokenStream
    
    # Создаем входной поток
    input_stream = InputStream(code)
    
    # Создаем лексер с обработкой отступов
    from indentation_lexer import IndentationLexer
    lexer = IndentationLexer(input_stream)
    
    # Создаем поток токенов
    stream = CommonTokenStream(lexer)
    
    # Создаем парсер
    parser = vecmatlangParser(stream)
    
    # Строим AST
    tree = parser.program()
    
    # Создаем анализатор
    analyzer = SemanticAnalyzer()
    
    # Обходим дерево
    from antlr4.tree.Tree import ParseTreeWalker
    walker = ParseTreeWalker()
    walker.walk(analyzer, tree)
    
    return analyzer.errors, analyzer.warnings

# ========== Пример использования ==========

if __name__ == "__main__":
    example_code = """
func swap(a, b): # перегрузка подпрограммы по количеству аргументов
    return b, a

func swap(a, b, c):
    return b, c, a

x = [1, 2, 3]
y = [4, 5]

# многоцелевой оператор присваивания
x, y = swap(x, y)  

a = 1
b = 2
c = 3
a, b, c = swap(a, b, c)
"""
    
    errors, warnings = analyze_code(example_code)
    
    print("=== Результаты семантического анализа ===")
    print(f"Найдено ошибок: {len(errors)}")
    print(f"Найдено предупреждений: {len(warnings)}")
    
    if errors:
        print("\nОшибки:")
        for error in errors:
            print(f"  {error}")
            
    if warnings:
        print("\nПредупреждения:")
        for warning in warnings:
            print(f"  {warning}")