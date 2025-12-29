# semantic_analyzer.py
from typing import Dict, List, Optional, Tuple
from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker

from generated.vecmatlangParser import vecmatlangParser
from generated.vecmatlangListener import vecmatlangListener

from syntax_analyzer import read_vml, get_analyze_tools, EXAMPLES_DIR
from symbols import Type, Symbol, FunctionSymbol, ClassSymbol

EXAMPLES_NAMES = [
    'example1.vml',
    'example2.vml',
    'example3.vml',
    'example4.vml',
    'wrongsemantic_example1.vml',
    'wrongsemantic_example2.vml',
    'wrongsemantic_example3.vml'
]


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
        self.in_method = False  # внутри метода класса
        self.class_params = {}  # Параметры текущего класса
        self.last_constructor_call = None


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

#         print(f"DEBUG: Начало объявления функции {ctx.ID().getText()} на строке {ctx.start.line}")

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
            param_ids = param_list.ID()
            params = [Type.UNKNOWN] * len(param_ids)
        
        # Ищем существующую функцию
        existing_symbol = self._lookup_symbol(func_name)
        func_sym = None
        
        if existing_symbol:
            if isinstance(existing_symbol, FunctionSymbol):
                # Добавляем перегрузку к существующей функции
                existing_symbol.add_overload(params)
                self._add_warning(f"Перегрузка функции '{func_name}' с {len(params)} параметрами", line, column)
                func_sym = existing_symbol  # Используем существующий символ
            else:
                self._add_error(f"Имя '{func_name}' уже используется для другой сущности", line, column)
                return
        else:
            # Создаем новую функцию
            func_sym = FunctionSymbol(func_name, return_type, params, line, column)
            self.symbol_table[func_name] = func_sym
        
#             print(f'DEBUG: Функция {func_name} с аргументами {params} была добавлена в таблицу символов')

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

#         print(f'DEBUG: Класс {class_name} был добавлен в таблицу символов')

#         print(f'DEBUG: {self.symbol_table}')
        
        # Сохраняем параметры класса
        self.class_params = {}
        param_list = ctx.parameterList()
        if param_list:
            for param in param_list.ID():
                param_name = param.getText()
                self.class_params[param_name] = Type.UNKNOWN
                # Сохраняем в классе
                class_sym.add_constructor_param(param_name)
        
        # Входим в область видимости класса (для инициализации полей)
        self._enter_scope()
        
        # Добавляем параметры класса в область видимости
        for param_name in self.class_params:
            param_symbol = Symbol(param_name, Type.UNKNOWN, ctx.start.line, ctx.start.column)
            param_symbol.is_initialized = True  # Параметры считаются инициализированными
            self._current_scope_table()[param_name] = param_symbol
        
        # Создаем неявный конструктор
        constructor_params = list(self.class_params.keys())
        constructor_name = f'{class_name}_constructor'
        constructor = FunctionSymbol(constructor_name , Type.CLASS, 
                                    [Type.UNKNOWN] * len(constructor_params),
                                    line, column)
        self.symbol_table[constructor_name] = constructor  # Конструктор доступен глобально

#         print(f'DEBUG: конструктор {constructor_name} был добавлен в таблицу символов')
        
    def exitClassDecl(self, ctx: vecmatlangParser.ClassDeclContext):
        # Выходим из области видимости инициализации полей
        self._exit_scope()
        
        # Сбрасываем состояние
        self.current_class = None
        self.in_class_body = False
        self.class_params = {}
        
    def enterMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        """Вход в объявление метода"""
            
        method_name = ctx.ID().getText()
        line = ctx.start.line
        column = ctx.start.column
        
        # Парсим параметры метода
        params = []
        param_list = ctx.parameterList()
        if param_list:
            params = [Type.UNKNOWN] * len(param_list.ID())
            
        # Проверяем, не перекрывают ли параметры поля класса
        if param_list:
            for param in param_list.ID():
                param_name = param.getText()
                # Проверяем, есть ли поле с таким именем в классе
                if self.current_class and param_name in self.current_class.fields:
                    self._add_error(f"Параметр метода '{param_name}' перекрывает поле класса с тем же именем", 
                                  param.symbol.line, param.symbol.column)

        # Создаем символ метода
        method_sym = FunctionSymbol(method_name, Type.UNKNOWN, params, line, column, True)
        
        # Добавляем метод в класс
        self.current_class.methods[method_name] = method_sym

#         print(f'DEBUG: Метод {method_name} с аргументами {params} был добавлен в класс {self.current_class}')
        
        # Устанавливаем текущий метод
        self.current_function = method_sym
        self.in_method = True
        
        # Входим в область видимости метода
        self._enter_scope()
        
        # Добавляем неявный параметр self для доступа к полям класса
        self._current_scope_table()["self"] = Symbol("self", Type.CLASS, line, column)
        self._current_scope_table()["self"].is_initialized = True
        
        # Добавляем параметры метода
        if param_list:
            for param in param_list.ID():
                param_name = param.getText()
                param_symbol = Symbol(param_name, Type.UNKNOWN, 
                                    param.symbol.line, param.symbol.column)
                param_symbol.is_initialized = True
                self._current_scope_table()[param_name] = param_symbol
                
    def exitMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        """Выход из объявления метода"""
        self.in_method = False
        self.current_function = None
        self._exit_scope()
        
    # ========== Обработка присваиваний ==========
    
    def enterSingleAssignment(self, ctx: vecmatlangParser.SingleAssignmentContext):

        var_ctx = ctx.var()
        expr_ctx = ctx.expression()
        
        # Определяем имя переменной
        var_name = self._get_var_name(var_ctx)
        if not var_name:
            return
        
        self.last_constructor_call = None
            
        # Анализируем тип выражения
        expr_type = self._analyze_expression(expr_ctx)

#         print(f'DEBUG: {expr_type}')
        
        # Если это простое имя переменной (не поле класса)
        if ctx.var().ID():
            # Проверяем, объявлена ли уже переменная
            existing_symbol = self._lookup_symbol(var_name)
            
            if not existing_symbol:
                # Если не объявлена - добавляем в текущую область видимости
                new_symbol = Symbol(var_name, expr_type, ctx.start.line, ctx.start.column)
                new_symbol.is_initialized = True

                # Если это объект класса, сохраняем ссылку на класс
                if expr_type == Type.CLASS and self.last_constructor_call:
                    # Сохраняем имя класса в переменной
                    # Можно добавить поле class_name в Symbol
                    new_symbol.class_ref = self.last_constructor_call
#                     print(f'DEBUG: Переменная {var_name} типа CLASS ссылается на класс {self.last_constructor_call}')

                self._current_scope_table()[var_name] = new_symbol

#                 print(f'DEBUG: Объект {var_name} был добавлен в текущую область видимости {self.current_scope}')
            else: existing_symbol.is_initialized = True
                
        # Если это обращение к полю класса (obj.field)
        elif ctx.var().fieldAppeal():
            # Проверяем, что поле существует и доступно для записи
            field_name_parts = var_name.split('.')
            if len(field_name_parts) == 2:
                obj_name, field_name = field_name_parts
                
                # Находим объект
                obj_symbol = self._lookup_symbol(obj_name)
                if obj_symbol and obj_symbol.type == Type.CLASS:
                    # ДОПОЛНЕНИЕ: Проверка на перезапись поля вне класса
                    self._add_error(f"Поле '{field_name}' объекта '{obj_name}' изменяется вне класса", 
                                    var_ctx.start.line, var_ctx.start.column)
                    
                if not obj_symbol or obj_symbol.type != Type.CLASS:
                    self._add_error(f"Объект '{obj_name}' не найден",
                                  var_ctx.start.line, var_ctx.start.column)
                    return
                    
                # Находим класс
                class_name = obj_symbol.class_ref
                class_sym = self.symbol_table.get(class_name)

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
                    
        else:
            # Для индексированных переменных пока пропускаем проверку
            pass

         # Если это внутри тела класса (инициализация поля)
        if self.in_class_body and not self.in_method:
            if '.' not in var_name:  # Не обращение к полю другого объекта
                # Это инициализация поля класса
                if self.current_class:
                    # Проверяем, что поле инициализируется параметром класса или выражением
                    self.current_class.add_field(var_name, expr_type, 
                                                var_ctx.start.line, var_ctx.start.column)
                    
                    # Отмечаем поле как инициализированное
                    field_symbol = Symbol(var_name, expr_type, 
                                         var_ctx.start.line, var_ctx.start.column)
                    field_symbol.is_initialized = True
                    self._current_scope_table()[var_name] = field_symbol

#                     print(f'DEBUG: Поле {var_name} было добавлено в текущий класс {self.current_class}')
                
    def enterMultipleAssignment(self, ctx: vecmatlangParser.MultipleAssignmentContext):
        """Обработка множественного присваивания: x, y = swap(x, y)"""
        
        # Получаем переменные слева
        var_nodes = []
        if hasattr(ctx, 'var') and ctx.var():
            # Получаем все var узлы
            var_nodes = []
            # В грамматике multipleAssignment: var (',' var)+ '=' primaryExpression
            # Первый var уже есть
            first_var = ctx.var(0)
            var_nodes.append(first_var)
            
            # Ищем дополнительные var через детей контекста
            for i in range(1, ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, vecmatlangParser.VarContext):
                    var_nodes.append(child)
        
        # Получаем выражение справа
        if hasattr(ctx, 'primaryExpression'):
            expr = ctx.primaryExpression()
            expr_type = self._analyze_primary_expression(expr)
            
            # Если это вызов функции
            if isinstance(expr, vecmatlangParser.FuncCallExprContext):
                func_name = expr.ID().getText()
                func_symbol = self._lookup_symbol(func_name)
                
                if isinstance(func_symbol, FunctionSymbol):
                    # Определяем количество аргументов в вызове
                    arg_list = expr.argumentList()
                    arg_count = len(arg_list.expression()) if arg_list else 0
                    

                    expected_returns = arg_count
                    actual_vars = len(var_nodes)
                    
                    if expected_returns != actual_vars:
                        self._add_error(f"Функция '{func_name}' возвращает {expected_returns} значений, " +
                                    f"но присваивается {actual_vars} переменным",
                                    ctx.start.line, ctx.start.column)
        
        # Добавляем/обновляем переменные
        for var_node in var_nodes:
            if var_node.ID():
                var_name = var_node.ID().getText()
                existing_symbol = self._lookup_symbol(var_name)
                
                if not existing_symbol:
                    # Создаем новую переменную с типом UNKNOWN
                    new_symbol = Symbol(var_name, Type.UNKNOWN, var_node.start.line, var_node.start.column)
                    new_symbol.is_initialized = True
                    self._current_scope_table()[var_name] = new_symbol

#                     print(f'DEBUG: Переменная {var_name} была добавлена в текущую область видимости {self.current_scope}')
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

#         print(f'DEBUG: Анализ выражения "{expr_ctx.getText()}"')

        if isinstance(expr_ctx, vecmatlangParser.PrimaryExprContext):
#             print('---DEBUG: Это первичное выражение')

            return self._analyze_primary_expression(expr_ctx.primaryExpression())

        elif isinstance(expr_ctx, vecmatlangParser.UnaryMinusExprContext):

#             print('---DEBUG: Это выражение с унарным минусом')

            inner_type = self._analyze_expression(expr_ctx.expression())
            if inner_type not in [Type.INT, Type.FLOAT, Type.VECTOR, Type.MATRIX]:

#                 print('===SEM_ERROR')
                self._add_error("Унарный минус применяется только к числам, векторам и матрицам", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
            return inner_type
        elif isinstance(expr_ctx, vecmatlangParser.IndexExprContext):

#             print('---DEBUG: Это выражение с индексацией')
            # Индексация: expr[expr]
            obj_type = self._analyze_expression(expr_ctx.expression(0))
            index_type = self._analyze_expression(expr_ctx.expression(1))
            
            if index_type != Type.INT:
#                 print('===SEM_ERROR')
                self._add_error(f"Индекс должен быть int, получен {index_type.value}", 
                              expr_ctx.start.line, expr_ctx.start.column)
                
            if obj_type == Type.VECTOR:
                return Type.FLOAT
            elif obj_type == Type.MATRIX:
                return Type.VECTOR
            else:
#                 print('===SEM_ERROR')
                self._add_error("Индексация применяется только к vector и matrix", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
        elif isinstance(expr_ctx, (vecmatlangParser.MulDivExprContext, 
                                  vecmatlangParser.AddSubExprContext,
                                  vecmatlangParser.ComparisonExprContext,
                                  vecmatlangParser.BinlogicExprContext)):
            
#             print('---DEBUG: Это бинарное выражение')

            return self._analyze_binary_op(expr_ctx)
        elif isinstance(expr_ctx, vecmatlangParser.NotExprContext):

#             print('---DEBUG: Это выражение с отрицанием')

            inner_type = self._analyze_expression(expr_ctx.expression())
            if inner_type != Type.BOOL:
#                 print('===SEM_ERROR')
                self._add_error("Оператор '!' применяется только к bool", 
                              expr_ctx.start.line, expr_ctx.start.column)
                return Type.UNKNOWN
            return Type.BOOL
            
#         print('---DEBUG: Это неизвестное выражение')
        
        return Type.UNKNOWN
        
    def _analyze_binary_op(self, expr_ctx) -> Type:
        """Анализ бинарной операции"""
        left_type = self._analyze_expression(expr_ctx.expression(0))
        right_type = self._analyze_expression(expr_ctx.expression(1))
        
        # Определяем оператор
        op_text = expr_ctx.getChild(1).getText()
        
        # Для всех бинарных операций используем общую функцию
        return self._get_binary_op_result_type(left_type, right_type, op_text,
                                            expr_ctx.start.line, expr_ctx.start.column)
        
    def _analyze_primary_expression(self, primary_ctx) -> Type:
        """Анализ первичного выражения"""

        if isinstance(primary_ctx, vecmatlangParser.VarExprContext):
            # Идентификатор или переменная

#             print('   ---DEBUG: Это переменная')
            var_ctx = primary_ctx.var()

            if var_ctx.fieldAppeal():
                # Обращение к полю класса: obj.field
#                 print('   ---DEBUG: Это обращение к полю класса внутри VarExpr')
                return self._analyze_field_access(var_ctx.fieldAppeal())

            elif var_ctx.ID():

                var_name = var_ctx.ID().getText()
                symbol = self._lookup_symbol(var_name)

                if self.in_method and not symbol:
                    # Если внутри метода и символ не найден
                    # Проверяем, не является ли это параметром конструктора класса
                    if self.current_class and var_name in self.current_class.constructor_params:
                        # Это параметр конструктора класса, используемый в методе
                        self._add_error(f"Параметр конструктора '{var_name}' недоступен в методах класса", 
                                      primary_ctx.start.line, primary_ctx.start.column)
                        return Type.UNKNOWN
                
                if not symbol:  
                    if self.in_method:
                        # Проверяем, не является ли это обращением к полю класса
                        if self.current_class and var_name in self.current_class.fields:
                            # Это обращение к полю класса (без self.)
                            field = self.current_class.fields[var_name]
                            return field.type


#                     print('   ===SEM_ERROR')
                    self._add_error(f"Идентификатор '{var_name}' не найден", 
                                  primary_ctx.start.line, primary_ctx.start.column)
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
                    
                func_in_table = self.symbol_table.get(var_name)

                if isinstance(func_in_table, FunctionSymbol):
                    # Это функция, уже объявленная где-то
                    return Type.UNKNOWN  # или func_in_table.type
                
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
                
            elif var_ctx.getChildCount() > 1 and var_ctx.getChild(1).getText() == '[':
                # Индексированная переменная: arr[index]
                # Обработка индексации
                obj_name = var_ctx.ID().getText()
                symbol = self._lookup_symbol(obj_name)
                if not symbol:
                    self._add_error(f"Переменная '{obj_name}' не найдена", 
                                  var_ctx.start.line, var_ctx.start.column)
                    return Type.UNKNOWN
                    
                if symbol.type not in [Type.VECTOR, Type.MATRIX]:
                    self._add_error(f"Индексация применяется только к vector и matrix, а не к {symbol.type.value}", 
                                  var_ctx.start.line, var_ctx.start.column)
                    return Type.UNKNOWN
                    
                # Для вектора возвращаем FLOAT, для матрицы - VECTOR
                if symbol.type == Type.VECTOR:
                    return Type.FLOAT
                else:  # MATRIX
                    return Type.VECTOR
                
        elif isinstance(primary_ctx, vecmatlangParser.ParenExprContext):
#             print('   ---DEBUG: Это выражение со скобками')
            return self._analyze_expression(primary_ctx.expression())
            
        elif isinstance(primary_ctx, vecmatlangParser.FuncCallExprContext):
#             print('    ---DEBUG: Это выражение вызова функции')
            return self._analyze_function_call(primary_ctx)
            
        elif isinstance(primary_ctx, vecmatlangParser.MethodExprContext):
#             print('    ---DEBUG: Это выражение вызова метода')
            return self._analyze_method_call(primary_ctx.methodAppeal())
            
        elif isinstance(primary_ctx, vecmatlangParser.LiteralExprContext):
#             print('    ---DEBUG: Это выражение-литерал')
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
#                         print('    ===SEM_ERROR')
                        self._add_error(f"Вектор может содержать только числа", 
                                      primary_ctx.start.line, primary_ctx.start.column)
                        
            return target_type
            
        elif isinstance(primary_ctx, vecmatlangParser.LenExprContext):
            # len() функция
            arg_list = primary_ctx.argumentList()
            if not arg_list or len(arg_list.expression()) != 1:
#                 print('    ===SEM_ERROR')
                self._add_error("Функция len() принимает ровно один аргумент", 
                              primary_ctx.start.line, primary_ctx.start.column)
                return Type.UNKNOWN
                
            arg_type = self._analyze_expression(arg_list.expression(0))
            if arg_type not in [Type.VECTOR, Type.MATRIX]:
#                 print('   ===SEM_ERROR')
                self._add_error("Функция len() применяется только к vector и matrix", 
                              primary_ctx.start.line, primary_ctx.start.column)
                return Type.UNKNOWN
                
            return Type.INT
            
        elif isinstance(primary_ctx, vecmatlangParser.ReadExprContext):
            return Type.STRING
            
        return Type.UNKNOWN
        
    def _analyze_field_access(self, field_ctx) -> Type:
        """Анализ обращения к полю класса: obj.field"""
#         print(f"DEBUG _analyze_field_access: {field_ctx.getText()}")
        
        obj_name = field_ctx.ID(0).getText()
        field_name = field_ctx.ID(1).getText()
        
        # Проверяем, что объект существует
        obj_symbol = self._lookup_symbol(obj_name)
        if not obj_symbol:
#             print(f"DEBUG: Объект '{obj_name}' не найден")
            self._add_error(f"Объект '{obj_name}' не найден", 
                          field_ctx.start.line, field_ctx.start.column)
            return Type.UNKNOWN
            
        # Проверяем тип объекта
        if obj_symbol.type != Type.CLASS:
#             print(f"DEBUG: '{obj_name}' не является объектом класса")
            self._add_error(f"'{obj_name}' не является объектом класса (тип: {obj_symbol.type.value})", 
                          field_ctx.start.line, field_ctx.start.column)
            return Type.UNKNOWN
        
        # Определяем класс объекта
        class_name = None
        
        # Способ 1: из поля class_ref в Symbol
        if hasattr(obj_symbol, 'class_ref') and obj_symbol.class_ref:
            class_name = obj_symbol.class_ref
        
#         print(f"DEBUG: Предполагаемый класс для '{obj_name}': '{class_name}'")
        
        if not class_name:
            self._add_error(f"Не удалось определить класс объекта '{obj_name}'", 
                          field_ctx.start.line, field_ctx.start.column)
            return Type.UNKNOWN
        
        # Находим класс
        class_sym = self.symbol_table.get(class_name)
        if not isinstance(class_sym, ClassSymbol):
#             print(f"DEBUG: Класс '{class_name}' не найден или не ClassSymbol")
            self._add_error(f"Класс '{class_name}' не найден для объекта '{obj_name}'", 
                          field_ctx.start.line, field_ctx.start.column)
            return Type.UNKNOWN
            
#         print(f"DEBUG: Поля класса {class_name}: {list(class_sym.fields.keys())}")
#         print(f"DEBUG: Ищем поле '{field_name}'")
        
        # Проверяем поле
        field = class_sym.fields.get(field_name)
        if not field:
#             print(f"DEBUG: Поле '{field_name}' не найдено")
            self._add_error(f"Поле '{field_name}' не найдено в классе '{class_name}'", 
                          field_ctx.start.line, field_ctx.start.column)
            return Type.UNKNOWN
            
#         print(f"DEBUG: Поле '{field_name}' найдено, тип: {field.type}")
        return field.type
        
    def _analyze_method_call(self, method_ctx) -> Type:
        """Анализ вызова метода класса: obj.method()"""
        obj_name = method_ctx.ID(0).getText()
        method_name = method_ctx.ID(1).getText()

#         print(f'DEBUG: Анализ вызова метода {method_name}')
        
        # Проверяем объект
        obj_symbol = self._lookup_symbol(obj_name)
        if not obj_symbol:
            self._add_error(f"Объект '{obj_name}' не найден", 
                          method_ctx.start.line, method_ctx.start.column)
            return Type.UNKNOWN
            
        # Получаем класс
        class_sym = self.symbol_table.get(obj_name)
        if not isinstance(class_sym, ClassSymbol):
            # Проверяем, не является ли это конструктором
            constructor = self.symbol_table.get(obj_name)
            if isinstance(constructor, FunctionSymbol) and constructor.type == Type.CLASS:
                self._add_error(f"Нельзя вызывать методы у конструктора класса", 
                              method_ctx.start.line, method_ctx.start.column)
                return Type.UNKNOWN
                
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
            for expr in arg_list.expression():
                self._analyze_expression(expr)
                
        return method.type  # Тип возвращаемого значения метода

    def _analyze_function_call(self, func_ctx) -> Type:
        """Анализ вызова функции"""

        func_name = func_ctx.ID().getText()
        line = func_ctx.start.line
        column = func_ctx.start.column

#         print(f"DEBUG: Анализ вызова функции {func_name} на строке {line}")

        # Анализируем аргументы
        arg_count = 0
        arg_list = func_ctx.argumentList()
        if arg_list:
            arg_count = len(arg_list.expression())
            for expr in arg_list.expression():
                self._analyze_expression(expr)  # Анализируем, но не проверяем типы строго
        
        # Проверяем, не является ли это конструктором класса
        class_sym = self.symbol_table.get(func_name)

#         print(f'DEBUG: {self.symbol_table}')

        if isinstance(class_sym, ClassSymbol):
                    
            # Проверяем количество параметров конструктора
            expected_params = len(class_sym.fields)  
            if arg_count != expected_params:
                self._add_error(f"Конструктор класса '{func_name}' ожидает {expected_params} аргументов, получено {arg_count}", 
                                line, column)
                                
            self.last_constructor_call = func_name

            return Type.CLASS  # Конструктор возвращает объект класса
            
        # Обработка обычных функций
        func_symbol = self._lookup_symbol(func_name)
        
        # КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: проверяем не только существование, но и тип символа
        if not func_symbol:
            # Символ не найден - это не функция, не переменная, ничего
            self._add_error(f"Идентификатор '{func_name}' не найден", line, column)
            return Type.UNKNOWN
            
        if not isinstance(func_symbol, FunctionSymbol):
            # Символ найден, но это не функция
            self._add_error(f"'{func_name}' не является функцией (это {func_symbol.type.value})", line, column)
            return Type.UNKNOWN
            
        
        # Для функций с перегрузками пытаемся найти подходящую по количеству аргументов
        matching_overload = func_symbol.find_matching_overload(arg_count)
        
        if not matching_overload:
            # Не найдена подходящая перегрузка
            overloads_info = func_symbol.get_all_overloads_info()
            
            # Если у функции нет перегрузок (или только одна), выдаем более точное сообщение
            if len(func_symbol.overloads) == 1:
                expected_args = len(func_symbol.overloads[0])
                self._add_error(f"Функция '{func_name}' ожидает {expected_args} аргументов, получено {arg_count}", 
                              line, column)
            else:
                self._add_error(f"Не найдена подходящая перегрузка функции '{func_name}'. " +
                            f"Вызвано с {arg_count} аргументами. " +
                            f"Доступные перегрузки: {overloads_info}", 
                            line, column)
            return Type.UNKNOWN
        
        # Для встроенных функций
        if func_name == "range":
            if arg_count < 1 or arg_count > 3:
                self._add_error("Функция range() принимает от 1 до 3 аргументов", line, column)
                return Type.UNKNOWN
            return Type.VECTOR
            
        elif func_name == "int":
            if arg_count != 1:
                self._add_error("Функция int() принимает ровно один аргумент", line, column)
                return Type.UNKNOWN
            return Type.INT
            
        elif func_name == "float":
            if arg_count != 1:
                self._add_error("Функция float() принимает ровно один аргумент", line, column)
                return Type.UNKNOWN
            return Type.FLOAT
            
        elif func_name == "write":
            # write может принимать любое количество аргументов
            return Type.VOID
            
        elif func_name == "read":
            # read может принимать 0 или 1 аргумент
            if arg_count > 1:
                self._add_error("Функция read() принимает не более одного аргумента", line, column)
            return Type.STRING
        
        # Для пользовательских функций с фиксированным количеством параметров
        # Проверяем соответствие количества аргументов
        if matching_overload and len(matching_overload) > 0:
            # Если функция имеет параметры, проверяем соответствие
            expected_args = len(matching_overload)
            if arg_count != expected_args:
                self._add_error(f"Функция '{func_name}' ожидает {expected_args} аргументов, получено {arg_count}", 
                              line, column)
        
        # Для пользовательских функций возвращаем UNKNOWN (динамическая типизация)
        return Type.UNKNOWN
        
    def _analyze_literal(self, literal_ctx) -> Type:
        """Анализ литерала"""
        
        if isinstance(literal_ctx, vecmatlangParser.IntLiteralContext): return Type.INT
        elif isinstance(literal_ctx, vecmatlangParser.FloatLiteralContext): return Type.FLOAT
        elif isinstance(literal_ctx, vecmatlangParser.StringLiteralContext): return Type.STRING
        elif isinstance(literal_ctx, vecmatlangParser.VectorLiteralContext): return self._analyze_vector_literal(literal_ctx)
        elif isinstance(literal_ctx, vecmatlangParser.MatrixLiteralContext): return self._analyze_matrix_literal(literal_ctx)
        
        return Type.UNKNOWN

    def _analyze_vector_literal(self, vector_ctx) -> Type:
        """Анализ векторного литерала"""
        
        text = vector_ctx.getText()
        
        # Проверяем, не является ли это на самом деле матрицей
        # (на случай если парсер ошибся)
        if text.startswith('[[') and text.endswith(']]'):
            # Это может быть матрица
            # Проверим элементы через argumentList
            arg_list = vector_ctx.argumentList()
            if arg_list:
                for expr in arg_list.expression():
                    # Если элемент содержит внутренние скобки, это может быть вектор
                    expr_text = expr.getText()
                    if expr_text.startswith('[') and expr_text.endswith(']'):
                        return Type.MATRIX
                        
        # Обычный анализ вектора
        arg_list = vector_ctx.argumentList()
        if not arg_list:
            return Type.VECTOR  # Пустой вектор []
        
        # Получаем все выражения из argumentList
        expressions = arg_list.expression()
        if not expressions:
            return Type.VECTOR  # Пустой вектор
        
        elem_types = []
        for expr in expressions:
            elem_type = self._analyze_expression(expr)
            
            if elem_type not in [Type.INT, Type.FLOAT, Type.VECTOR, Type.MATRIX]:
                self._add_error(f"Векторный элемент должен быть числом или вектором, получен {elem_type.value}", 
                            expr.start.line, expr.start.column)
                return Type.VECTOR
            elem_types.append(elem_type)
        
        # Определяем тип: если хотя бы один элемент - вектор, это матрица
        if any(t == Type.VECTOR for t in elem_types):
            
            # Проверяем, что все элементы - векторы одинаковой длины
            vector_lengths = []
            for expr in expressions:
                expr_text = expr.getText()
                # Если это векторный литерал
                if expr_text.startswith('[') and expr_text.endswith(']'):
                    # Подсчитываем элементы внутри вектора
                    # Простой подсчет запятых + 1
                    inner_text = expr_text[1:-1].strip()
                    if not inner_text:
                        vector_lengths.append(0)
                    else:
                        # Примерно считаем элементы
                        vector_lengths.append(inner_text.count(',') + 1)
            
            if vector_lengths:
                first_len = vector_lengths[0]
                for i, length in enumerate(vector_lengths[1:], 1):
                    if length != first_len:
                        self._add_error(f"Строки матрицы имеют разную длину: строка {i+1} имеет {length} элементов, строка 1 имеет {first_len}", 
                                    expr.start.line, expr.start.column)
            
            return Type.MATRIX
        elif any(t == Type.MATRIX for t in elem_types): 
            self._add_warning("Тензоры 3D и выше не поддерживаются", 
                            vector_ctx.start.line, vector_ctx.start.column)
            return Type.MATRIX  # Возвращаем как матрицу для совместимости
        
        # Определяем тип вектора на основе элементов
        if Type.FLOAT in elem_types:
            return Type.VECTOR  # вектор с float элементами
        return Type.VECTOR  # вектор с int элементами

    def _analyze_matrix_literal(self, matrix_ctx) -> Type:
        """Анализ матричного литерала"""
        
        # Матричный литерал в новой грамматике: '[' '[' argumentList ']' (',' '[' argumentList ']')* ']'
        # Нужно получить все строки матрицы (векторные литералы)
        
        # Собираем строки матрицы - ищем все VectorLiteralContext
        rows = []
        
        # Обходим детей контекста
        for i in range(matrix_ctx.getChildCount()):
            child = matrix_ctx.getChild(i)
            if isinstance(child, vecmatlangParser.VectorLiteralContext):
                rows.append(child)
        
        # Если не нашли через обход детей, попробуем другой способ
        if not rows:
            # В новой грамматике матрица состоит из векторных литералов
            # Получим текст и попробуем разобрать
            text = matrix_ctx.getText()
            if text.startswith('[[') and text.endswith(']]'):
                inner = text[2:-2].strip()
                # Пока пропустим детальный анализ
                pass
        
        # Проверяем строки
        if rows:
            row_lengths = []
            elem_types = set()
            
            for i, row_ctx in enumerate(rows):
                arg_list = row_ctx.argumentList()
                if not arg_list:
                    self._add_error(f"Строка матрицы {i+1} пустая", 
                                row_ctx.start.line, row_ctx.start.column)
                    continue
                    
                expressions = arg_list.expression()
                if not expressions:
                    self._add_error(f"Строка матрицы {i+1} пустая", 
                                row_ctx.start.line, row_ctx.start.column)
                    continue
                    
                row_lengths.append(len(expressions))
                
                for expr in expressions:
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
        
        return Type.MATRIX
        
    # ========== Проверки совместимости типов ==========
    
    def _get_binary_op_result_type(self, left: Type, right: Type, op: str, line: int, col: int) -> Type:
        """Определяет тип результата бинарной операции для динамически типизированного языка"""
        
        # Если любой из типов UNKNOWN, результат UNKNOWN (в динамической типизации)
        if left == Type.UNKNOWN or right == Type.UNKNOWN:
            return Type.UNKNOWN
        
        # Операция модуля/нормы (унарная) - обрабатывается отдельно в normExpr
        if op == '|':  # Для унарного ||
            if left in [Type.INT, Type.FLOAT]:
                return left  # |int| = int, |float| = float
            elif left == Type.VECTOR:
                return Type.FLOAT  # Норма вектора - float
            elif left == Type.MATRIX:
                return Type.FLOAT  # Норма матрицы - float
            else:
                return Type.UNKNOWN
        
        # Арифметические операции: +, -, *, /
        if op in ['+', '-', '*', '/']:
            # 1. Числовые операции
            if left in [Type.INT, Type.FLOAT] and right in [Type.INT, Type.FLOAT]:
                if op == '/':
                    # Деление всегда возвращает float
                    return Type.FLOAT
                elif left == Type.FLOAT or right == Type.FLOAT:
                    return Type.FLOAT
                else:
                    return Type.INT
            
            # 2. Векторные операции
            elif left == Type.VECTOR and right == Type.VECTOR:
                if op in ['+', '-']:
                    return Type.VECTOR
                elif op == '*':
                    return Type.FLOAT  # Скалярное произведение
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
            
            # 3. Вектор и число
            elif left == Type.VECTOR and right in [Type.INT, Type.FLOAT]:
                if op in ['*', '/']:
                    return Type.VECTOR  # Поэлементные операции
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN

                    
            elif left in [Type.INT, Type.FLOAT] and right == Type.VECTOR:
                if op == '*':
                    return Type.VECTOR
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
            
            
            # 4. Матричные операции
            elif left == Type.MATRIX and right == Type.MATRIX:
                if op in ['+', '-']:
                    return Type.MATRIX
                elif op == '*':
                    return Type.MATRIX  # Матричное умножение
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
            
            # 5. Матрица и число
            elif left == Type.MATRIX and right in [Type.INT, Type.FLOAT]:
                if op in ['*', '/']:
                    return Type.MATRIX  # Поэлементные операции
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
                    
            elif left in [Type.INT, Type.FLOAT] and right == Type.MATRIX:
                if op == '*':
                    return Type.MATRIX
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
            
            # 6. Матрица и вектор
            elif left == Type.MATRIX and right == Type.VECTOR:
                if op == '*':
                    return Type.VECTOR  # Умножение матрицы на вектор
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
                    
            elif left == Type.VECTOR and right == Type.MATRIX:
                if op == '*':
                    return Type.VECTOR  # Упрощенно
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
            
            # 7. Строковые операции
            elif left == Type.STRING:
                if right == Type.STRING and op == '+':
                    return Type.STRING  # Конкатенация строк
                elif op == '*' and right == Type.INT:
                    return Type.STRING  # Повторение строки
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
                    
            elif right == Type.STRING:
                if left == Type.INT and op == '*':
                    return Type.STRING  # Повторение строки
                else:
                    self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
                    return Type.UNKNOWN
        
        # Операции сравнения: >, <, >=, <=, ==, !=
        elif op in ['>', '<', '>=', '<=', '==', '!=']:
            # Сравнение всегда возвращает bool
            # В динамической типизации можно сравнивать разные типы
            return Type.BOOL
        
        # Логические операции: &&, ||
        elif op in ['&&', '||']:
            # Логические операции требуют bool
            if left == Type.BOOL and right == Type.BOOL:
                return Type.BOOL
            else:
                self._add_error(f"Логическая операция '{op}' применяется только к bool, получены {left.value} и {right.value}", 
                            line, col)
                return Type.UNKNOWN
        
        # Если операция не поддерживается для данных типов
        self._add_error(f"Операция '{op}' не поддерживается между {left.value} и {right.value}", line, col)
        return Type.UNKNOWN
        
    def _are_types_comparable(self, left: Type, right: Type) -> bool:
        """Можно ли сравнивать типы"""
        # В динамической типизации можно сравнивать почти любые типы
        # Возвращаем True, но выводим предупреждение для странных сравнений
        
        # Некоторые типы нельзя сравнивать осмысленно
        if left == Type.VOID or right == Type.VOID:
            return False  # void нельзя сравнивать
            
        if left == Type.CLASS and right != Type.CLASS:
            return False  # Класс можно сравнивать только с классом
            
        return True
        
    # ========== Обработка переменных ==========
    
    def enterVar(self, ctx: vecmatlangParser.VarContext):
        """Обработка использования переменной (например, в индексации)"""
        if ctx.ID():
            var_name = ctx.ID().getText()
            symbol = self._lookup_symbol(var_name)
            
            if not symbol:
                # ИЗМЕНЕНИЕ: Проверяем контекст
                # Получаем родительский контекст
                parent = ctx.parentCtx
                if parent and hasattr(parent, 'parentCtx'):
                    parent_parent = parent.parentCtx
                    if parent_parent and isinstance(parent_parent, vecmatlangParser.FuncCallExprContext):
                        # Это идентификатор в вызове функции
                        # Не создаем символ
                        return
                
                # Создаем символ с типом UNKNOWN, если переменная используется до объявления
                # (например, в индексации: a[i] где i еще не объявлен)
                symbol = Symbol(var_name, Type.UNKNOWN, ctx.start.line, ctx.start.column)
                self._current_scope_table()[var_name] = symbol
            elif not symbol.is_initialized:
                self._add_error(f"Переменная '{var_name}' используется до инициализации",
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
            
        # Проверяем количество аргументов
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


def analyze(file_path: str) -> Tuple[List[str], List[str]]:
    """Анализирует код и возвращает ошибки и предупреждения"""
    
    code = read_vml(file_path)

    lexer, parser, _ = get_analyze_tools(code)
    
    tree = parser.program()
    
    analyzer = SemanticAnalyzer()
    
    walker = ParseTreeWalker()
    walker.walk(analyzer, tree)
    
    return analyzer.errors, analyzer.warnings

if __name__ == "__main__":
    
    pathes = [EXAMPLES_DIR + file_name for file_name in EXAMPLES_NAMES]

    for file_path in pathes:

        print(f'\nНачало анализа {file_path}')
        errors, warnings = analyze(file_path)

        if errors:
            print("Ошибки в семантике:")
            for error in errors:
                print(f"  {error}")
                
        if warnings:
            print("Предупреждения (не нарушают семантику, но могут привести к ошибкам во время исполнения):")
            for warning in warnings:
                print(f"  {warning}")
        
        print(f"Анализ {file_path} завершен успешно. Количество семантических ошибок: {len(errors)}, количество предупреждений: {len(warnings)}")
        
    