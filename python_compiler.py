from generated.vecmatlangParser import vecmatlangParser
from generated.vecmatlangListener import vecmatlangListener

from semantic_analyzer import Type, FunctionSymbol

class PythonCompiler(vecmatlangListener):
    def __init__(self):
        super().__init__()
        self.output = []
        self.indent_level = 1 # отступ первого уровня, поскольку программа компилируется в функцию _main_
        self.current_class = None
        self.current_function = None
        self.current_method = False
        self.in_class_body = False
        self.in_class_init = False
        self.local_vars = set()
        self.class_fields = set()
        self.function_params = []
        self.temp_var_counter = 0
        self.loop_stack = []
        self.symbol_table = {}

        self.function_counter = {}  # Для отслеживания перегруженных функций
        self.current_function_base_name = None
        
        # Инициализация встроенных функций
        self._init_builtins()
        
    def _init_builtins(self):
        """Инициализация встроенных функций Python"""
        self.symbol_table['len'] = FunctionSymbol('len', Type.INT, [Type.UNKNOWN], 0, 0)
        self.symbol_table['write'] = FunctionSymbol('write', Type.VOID, [], 0, 0)
        self.symbol_table['read'] = FunctionSymbol('read', Type.STRING, [], 0, 0)
        self.symbol_table['range'] = FunctionSymbol('range', Type.VECTOR, [Type.INT], 0, 0)
        self.symbol_table['range'].add_overload([Type.INT, Type.INT])
        self.symbol_table['range'].add_overload([Type.INT, Type.INT, Type.INT])
        
    def _indent(self):
        return " " * (self.indent_level * 4)
    
    def _add_line(self, line):
        self.output.append(self._indent() + line)
    
    def _add_raw_line(self, line):
        self.output.append(line)
    
    def _generate_temp_var(self):
        temp = f"_tmp{self.temp_var_counter}"
        self.temp_var_counter += 1
        return temp
    
    # ========== Обработка программы ==========
    
    def enterProgram(self, ctx: vecmatlangParser.ProgramContext):
        # Добавляем импорты и указание кодировки
        self._add_raw_line("import numpy as np")
        self._add_raw_line("")
        
        # Устанавливаем кодировку для вывода
        self._add_raw_line("# -*- coding: utf-8 -*-")
        self._add_raw_line("")
        
        # Добавляем встроенные функции
        self._add_raw_line("# ========== Встроенные функции ==========")
        self._add_raw_line("def _vml_write(*args):")
        self._add_raw_line("    for arg in args:")
        self._add_raw_line("        # Убираем все лишние преобразования")
        self._add_raw_line("        print(str(arg), end='')")
        self._add_raw_line("    print()  # Добавляем перевод строки")
        self._add_raw_line("")
        
        self._add_raw_line("def _vml_read(prompt=''):")
        self._add_raw_line("    import sys")
        self._add_raw_line("    if sys.platform == 'win32':")
        self._add_raw_line("        import io")
        self._add_raw_line("        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')")
        self._add_raw_line("        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')")
        self._add_raw_line("    if prompt:")
        self._add_raw_line("        sys.stdout.write(str(prompt))")
        self._add_raw_line("        sys.stdout.flush()")
        self._add_raw_line("    return sys.stdin.readline().strip()")
        self._add_raw_line("")
        
        self._add_raw_line("def _vml_norm(x):")
        self._add_raw_line("    if isinstance(x, (int, float)):")
        self._add_raw_line("        return abs(x)")
        self._add_raw_line("    elif isinstance(x, np.ndarray):")
        self._add_raw_line("        return np.linalg.norm(x)")
        self._add_raw_line("    elif isinstance(x, list):")
        self._add_raw_line("        return np.linalg.norm(np.array(x, dtype=np.float64))")
        self._add_raw_line("    return 0")
        self._add_raw_line("")
        
        self._add_raw_line("def _vml_len(x):")
        self._add_raw_line("    if isinstance(x, list):")
        self._add_raw_line("        return len(x)")
        self._add_raw_line("    elif isinstance(x, np.ndarray):")
        self._add_raw_line("        if len(x.shape) == 1:")
        self._add_raw_line("            return x.shape[0]")
        self._add_raw_line("        else:")
        self._add_raw_line("            return x.shape[0]")
        self._add_raw_line("    return 0")
        self._add_raw_line("")
        
        self._add_raw_line("def _vml_vector_mult(a, b):")
        self._add_raw_line("    # Умножение векторов (скалярное) или вектора на число")
        self._add_raw_line("    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):")
        self._add_raw_line("        if len(a.shape) == 1 and len(b.shape) == 1:")
        self._add_raw_line("            return np.dot(a, b)")
        self._add_raw_line("    elif isinstance(a, np.ndarray) and isinstance(b, (int, float)):")
        self._add_raw_line("        return a * b")
        self._add_raw_line("    elif isinstance(a, (int, float)) and isinstance(b, np.ndarray):")
        self._add_raw_line("        return b * a")
        self._add_raw_line("    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):")
        self._add_raw_line("        return a * b  # Простое умножение чисел")
        self._add_raw_line("    return a * b")
        self._add_raw_line("")
        
        self._add_raw_line("def _vml_matrix_mult(a, b):")
        self._add_raw_line("    # Умножение матриц или матрицы на число/вектор")
        self._add_raw_line("    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):")
        self._add_raw_line("        if len(a.shape) == 2 and len(b.shape) == 2:")
        self._add_raw_line("            return np.dot(a, b)")
        self._add_raw_line("        elif len(a.shape) == 2 and len(b.shape) == 1:")
        self._add_raw_line("            return np.dot(a, b)")
        self._add_raw_line("    elif isinstance(a, np.ndarray) and isinstance(b, (int, float)):")
        self._add_raw_line("        return a * b")
        self._add_raw_line("    elif isinstance(a, (int, float)) and isinstance(b, np.ndarray):")
        self._add_raw_line("        return b * a")
        self._add_raw_line("    return a * b")
        self._add_raw_line("")
        
        # Переопределяем встроенные функции
        self._add_raw_line("write = _vml_write")
        self._add_raw_line("read = _vml_read")
        self._add_raw_line("")

        self._add_raw_line("def _main_():")

    
    # ========== Обработка функций ==========
    
    def enterFunctionDecl(self, ctx: vecmatlangParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        
        print(f'DEBUG: Enter in function {func_name} declaration')

        # Получаем параметры
        params = []
        if ctx.parameterList():
            for param in ctx.parameterList().ID():
                params.append(param.getText())
        
        # Определяем уникальное имя для перегруженной функции
        param_count = len(params)
        
        # Инициализируем счетчик для этой функции если нужно
        if func_name not in self.function_counter:
            self.function_counter[func_name] = {'count': 0, 'versions': {}}
        
        # Увеличиваем счетчик
        self.function_counter[func_name]['count'] += 1
        
        # Для обработки перегрузок добавляем суффикс
        actual_func_name = f"{func_name}_{param_count}arg"
        
        # Сохраняем информацию о версии
        self.function_counter[func_name]['versions'][param_count] = actual_func_name
        
        # Сохраняем информацию о текущей функции
        self.current_function_info = {
            'original_name': func_name,
            'actual_name': actual_func_name,
            'param_count': param_count
        }

        print(f'DEBUG: original: {func_name}, actual: {actual_func_name}, params: {param_count}')
        
        self.current_function = actual_func_name
        self.function_params = params
        self.local_vars = set(params)
        
        param_str = ", ".join(params)
        self._add_line(f"def {actual_func_name}({param_str}):")
        print(f'DEBUG: result: ({self.indent_level}) def {actual_func_name}({param_str}):')
        self.indent_level += 1
    
    def exitFunctionDecl(self, ctx: vecmatlangParser.FunctionDeclContext):
        if self.current_function:
            # Если функция не имеет return, добавляем неявный возврат None
            if self.output and not any(line.strip().startswith("return") for line in self.output[-5:]):
                self._add_line("return None")
            
            print(f'DEBUG: Exit from function declaration')

            self.current_function_base_name = None
            self.current_function = None
            self.function_params = []
            self.indent_level -= 1
            self._add_raw_line("")
    
    # ========== Обработка классов ==========
    
    def enterClassDecl(self, ctx: vecmatlangParser.ClassDeclContext):
        class_name = ctx.ID().getText()
        
        print(f'DEBUG: Enter in class {class_name} declaration')

        # Получаем параметры конструктора
        params = []
        if ctx.parameterList():
            for param in ctx.parameterList().ID():
                params.append(param.getText())
        
        self.current_class = class_name
        self.in_class_body = True
        self.in_class_init = False
        self.class_fields = set(params)  # Параметры конструктора
        
        # Определяем класс
        self._add_line(f"class {class_name}:")
        print(f'DEBUG: result: ({self.indent_level}) class {class_name}:')
        self.indent_level += 1
        
        # Добавляем конструктор
        param_str = ", ".join(["self"] + params)
        self._add_line(f"def __init__({param_str}):")
        print(f'DEBUG: result: ({self.indent_level}) def __init__({param_str}):')
        self.indent_level += 1
        
        # Теперь мы в конструкторе
        self.in_class_init = True
        
        # Сохраняем параметры как поля
        for param in params:
            self.local_vars.add(param)
        
        self.constructor_params = params

    def exitClassDecl(self, ctx: vecmatlangParser.ClassDeclContext):
        if self.current_class:
            # Выходим из класса
            print(f'DEBUG: Exit from class feclaration')
            self.indent_level -= 1
            self.current_class = None
            self.in_class_body = False
            self.class_fields = set()
            self.constructor_params = []
            self._add_raw_line("")

    def enterClassBody(self, ctx: vecmatlangParser.ClassBodyContext):
        """Вход в тело класса (после конструктора)"""
        
        print(f'DEBUG: Enter in classBody')

        # Теперь мы в теле класса
        self.in_class_body = True
        self._add_raw_line("")  # Пустая строка между конструктором и методами

    def exitClassBody(self, ctx: vecmatlangParser.ClassBodyContext):
        """Выход из тела класса"""
        print(f'DEBUG: Exit from classBody')
        self.in_class_body = False
        

    def enterMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        method_name = ctx.ID().getText()
        
        print(f'DEBUG: Enter in method {method_name} declaration')

        # Получаем параметры
        params = ["self"]  # Первый параметр - self
        if ctx.parameterList():
            for param in ctx.parameterList().ID():
                params.append(param.getText())
        
        self.current_method = True
        self.function_params = params
        self.local_vars = set(params)
        
        param_str = ", ".join(params)
        self._add_line(f"def {method_name}({param_str}):")
        print(f'DEBUG: result: ({self.indent_level}) def {method_name}({param_str}):')
        self.indent_level += 1

    def exitMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        if self.current_method:
            # Если метод не имеет return, добавляем неявный возврат None
            if self.output and not any(line.strip().startswith("return") for line in self.output[-5:]):
                self._add_line("return None")
            
            print(f'DEBUG: Exit from method declaration')

            self.current_method = False
            self.function_params = []
            self.indent_level -= 1
            self._add_raw_line("")

    def enterSingleAssignment(self, ctx: vecmatlangParser.SingleAssignmentContext):
        var_ctx = ctx.var()
        expr_ctx = ctx.expression()
        
        print(f'DEBUG: Enter in {ctx.getText()}')

        # Компилируем выражение
        expr_code = self._compile_expression(expr_ctx)
        
        # Получаем имя переменной
        if var_ctx.ID():
            var_name = var_ctx.ID().getText()
            
            # Проверяем контекст
            if self.in_class_init:
                # В конструкторе класса - это инициализация поля
                print('DEBUG: in constructor')

                self.class_fields.add(var_name)
                self._add_line(f"self.{var_name} = {expr_code}")
                print(f'DEBUG: result: ({self.indent_level}) self.{var_name} = {expr_code}')
                
            elif self.in_class_body and not self.current_method:
                # В теле класса, но вне методов - это объявление поля
                # В Python это обычно делается в конструкторе, но для совместимости
                # с VML мы можем создать поле в конструкторе
                self.class_fields.add(var_name)
                # Для простоты добавляем в конструктор
                # В реальности нужно было бы запомнить это для добавления в __init__
                pass  # Пропускаем, так как поля должны быть в конструкторе
                
            elif self.current_method:
                # В методе класса
                print(f'DEBUG: in method')

                if var_name in self.class_fields:
                    # Если это поле класса, используем self.
                    self._add_line(f"self.{var_name} = {expr_code}")
                    print(f'DEBUG: result: ({self.indent_level}) self.{var_name} = {expr_code}')
                else:
                    # Локальная переменная в методе
                    self.local_vars.add(var_name)
                    self._add_line(f"{var_name} = {expr_code}")
                    print(f'DEBUG: result: ({self.indent_level}) {var_name} = {expr_code}')
            else:
                # Глобальная или локальная переменная в функции
                print('DEBUG: in function')
                self.local_vars.add(var_name)
                self._add_line(f"{var_name} = {expr_code}")
                print(f'DEBUG: result: ({self.indent_level}) {var_name} = {expr_code}')

                
        elif var_ctx.fieldAppeal():
            print('DEBUG: in fieldAppeal')
            # Обращение к полю объекта: obj.field = expr
            field_appeal = var_ctx.fieldAppeal()
            obj_name = field_appeal.ID(0).getText()
            field_name = field_appeal.ID(1).getText()
            self._add_line(f"{obj_name}.{field_name} = {expr_code}")
            print(f'DEBUG: result: ({self.indent_level}) {obj_name}.{field_name} = {expr_code}')

    def enterMultipleAssignment(self, ctx: vecmatlangParser.MultipleAssignmentContext):
        # Получаем переменные слева
        vars_left = []
        var_ctxs = ctx.var()
        for var_ctx in var_ctxs:
            if var_ctx.ID():
                var_name = var_ctx.ID().getText()
                vars_left.append(var_name)

        print(f'DEBUG: Enter in {ctx.getText()}')
        
        # Компилируем правую часть
        if ctx.primaryExpression():
            # Если это вызов функции
            right_expr = self._compile_primary_expression(ctx.primaryExpression())
            self._add_line(f"{', '.join(vars_left)} = {right_expr}")
            print(f'DEBUG: result: ({self.indent_level}) {', '.join(vars_left)} = {right_expr}')
        else:
            # Если это список выражений
            exprs = []
            for expr_ctx in ctx.expression():
                exprs.append(self._compile_expression(expr_ctx))
            self._add_line(f"{', '.join(vars_left)} = {', '.join(exprs)}")
            print(f'DEBUG: result: ({self.indent_level}) {', '.join(vars_left)} = {', '.join(exprs)}')
    
    # ========== Компиляция выражений ==========
    
    def _compile_expression(self, ctx) -> str:
        try:
            if isinstance(ctx, vecmatlangParser.PrimaryExprContext):
                return self._compile_primary_expression(ctx.primaryExpression())
                
            elif isinstance(ctx, vecmatlangParser.UnaryMinusExprContext):
                inner = self._compile_expression(ctx.expression())
                return f"(-{inner})"
                
            elif isinstance(ctx, vecmatlangParser.NormExprContext):
                inner = self._compile_expression(ctx.expression())
                return f"_vml_norm({inner})"
                
            elif isinstance(ctx, vecmatlangParser.IndexExprContext):
                obj = self._compile_expression(ctx.expression(0))
                index = self._compile_expression(ctx.expression(1))
                return f"{obj}[{index}]"
                
            elif isinstance(ctx, vecmatlangParser.NotExprContext):
                inner = self._compile_expression(ctx.expression())
                return f"(not {inner})"
                
            elif isinstance(ctx, vecmatlangParser.ParenExprContext):
                inner = self._compile_expression(ctx.expression())
                return f"({inner})"
                
            elif isinstance(ctx, (vecmatlangParser.MulDivExprContext,
                                  vecmatlangParser.AddSubExprContext,
                                  vecmatlangParser.ComparisonExprContext,
                                  vecmatlangParser.BinlogicExprContext)):
                return self._compile_binary_op(ctx)
            
            return "None"
        except Exception as e:
            print(f"Ошибка компиляции выражения: {e}")
            return "None"
    
    def _compile_binary_op(self, ctx) -> str:
        left = self._compile_expression(ctx.expression(0))
        right = self._compile_expression(ctx.expression(1))
        
        # Убираем лишние скобки если они уже есть
        left_stripped = left.strip()
        right_stripped = right.strip()
        
        if left_stripped.startswith('(') and left_stripped.endswith(')'):
            left = left_stripped[1:-1]
        if right_stripped.startswith('(') and right_stripped.endswith(')'):
            right = right_stripped[1:-1]
        
        if isinstance(ctx, vecmatlangParser.MulDivExprContext):
            op = ctx.getChild(1).getText()
            # Специальная обработка умножения
            if op == '*':
                # Проверяем, нужно ли использовать специальные функции
                left_is_special = '_vml_matrix_mult' in left or '_vml_vector_mult' in left
                right_is_special = '_vml_matrix_mult' in right or '_vml_vector_mult' in right
                
                if left_is_special or right_is_special:
                    # Уже содержит специальную функцию
                    return f"({left} * {right})"
                elif self._is_likely_matrix(left) or self._is_likely_matrix(right):
                    return f"_vml_matrix_mult({left}, {right})"
                elif self._is_likely_vector_or_matrix(left) or self._is_likely_vector_or_matrix(right):
                    return f"_vml_vector_mult({left}, {right})"
                else:
                    return f"({left} * {right})"
            else:
                return f"({left} {op} {right})"
            
        elif isinstance(ctx, vecmatlangParser.AddSubExprContext):
            op = ctx.getChild(1).getText()
            # Для сложения/вычитания сохраняем скобки только если нужно
            if op == '+' and ('_vml_vector_mult' in left or '_vml_vector_mult' in right):
                return f"({left} {op} {right})"
            return f"{left} {op} {right}"
            
        elif isinstance(ctx, vecmatlangParser.ComparisonExprContext):
            op = ctx.getChild(1).getText()
            # Для сравнений не нужно добавлять внешние скобки
            return f"{left} {op} {right}"
            
        elif isinstance(ctx, vecmatlangParser.BinlogicExprContext):
            op = ctx.getChild(1).getText()
            if op == '&&':
                op = 'and'
            elif op == '||':
                op = 'or'
            return f"({left} {op} {right})"
    
    def _is_likely_vector_or_matrix(self, expr_code: str) -> bool:
        """Проверяет, вероятно ли выражение является вектором или матрицей"""
        if not expr_code:
            return False
        
        # Убираем лишние скобки для анализа
        expr_clean = expr_code.strip()
        while expr_clean.startswith('(') and expr_clean.endswith(')'):
            expr_clean = expr_clean[1:-1].strip()
        
        # Проверяем на простые числа
        if expr_clean.replace('.', '', 1).isdigit():
            return False
        
        expr_lower = expr_clean.lower()
        vector_indicators = ['np.array', 'vector', 'v1', 'v2', 'vec', 'sum_v', 'prod_m', 'm1', 'm2', 'vec_pair']
        
        # Проверяем на вызовы специальных функций
        if '_vml_' in expr_lower:
            return True
        
        return any(indicator in expr_lower for indicator in vector_indicators)
    
    def _is_likely_matrix(self, expr_code: str) -> bool:
        """Проверяет, вероятно ли выражение является матрицей"""
        if not expr_code:
            return False
        
        # Убираем лишние скобки для анализа
        expr_clean = expr_code.strip()
        while expr_clean.startswith('(') and expr_clean.endswith(')'):
            expr_clean = expr_clean[1:-1].strip()
        
        expr_lower = expr_clean.lower()
        matrix_indicators = ['np.array([np.array', 'matrix', 'm1', 'm2', 'prod_m']
        
        # Проверяем наличие двойных скобок
        if '[' in expr_clean and expr_clean.count('[') > 1:
            return True
            
        return any(indicator in expr_lower for indicator in matrix_indicators)
    
    def _compile_primary_expression(self, ctx) -> str:
        try:
            if isinstance(ctx, vecmatlangParser.VarExprContext):
                return self._compile_var(ctx.var())
                
            elif isinstance(ctx, vecmatlangParser.FuncCallExprContext):
                return self._compile_function_call(ctx)
                
            elif isinstance(ctx, vecmatlangParser.MethodExprContext):
                return self._compile_method_call(ctx.methodAppeal())
                
            elif isinstance(ctx, vecmatlangParser.LiteralExprContext):
                return self._compile_literal(ctx.literal())
                
            elif isinstance(ctx, vecmatlangParser.TypeExprContext):
                # Конструктор типа: int(x), float(x), vector([...]), matrix([[...]])
                type_name = ctx.type_().getText()
                args = []
                if ctx.argumentList():
                    for expr in ctx.argumentList().expression():
                        args.append(self._compile_expression(expr))
                
                if type_name == 'vector':
                    if args:
                        return f"np.array({args[0]}, dtype=np.float64)"
                    else:
                        return "np.array([], dtype=np.float64)"
                elif type_name == 'matrix':
                    if args:
                        return f"np.array({args[0]}, dtype=np.float64)"
                    else:
                        return "np.array([[]], dtype=np.float64)"
                elif type_name == 'int':
                    return f"int({args[0]})" if args else "0"
                elif type_name == 'float':
                    return f"float({args[0]})" if args else "0.0"
                
            elif isinstance(ctx, vecmatlangParser.LenExprContext):
                if ctx.argumentList() and len(ctx.argumentList().expression()) == 1:
                    arg = self._compile_expression(ctx.argumentList().expression(0))
                    return f"_vml_len({arg})"
                return "_vml_len(None)"
                
            elif isinstance(ctx, vecmatlangParser.ReadExprContext):
                args = []
                if ctx.readStatement().argumentList():
                    for expr in ctx.readStatement().argumentList().expression():
                        args.append(self._compile_expression(expr))
                
                if args:
                    return f"read({args[0]})"
                else:
                    return "read()"
            
            return "None"
        except Exception as e:
            print(f"Ошибка компиляции первичного выражения: {e}")
            import traceback
            traceback.print_exc()
            return "None"
    
    def _compile_var(self, var_ctx) -> str:
        """Компилирует переменную или обращение к полю"""
        if var_ctx.ID():
            var_name = var_ctx.ID().getText()
            # Проверяем, является ли это полем класса
            if self.current_method and var_name in self.class_fields:
                return f"self.{var_name}"
            else:
                return var_name
                
        elif var_ctx.fieldAppeal():
            field_appeal = var_ctx.fieldAppeal()
            obj_name = field_appeal.ID(0).getText()
            field_name = field_appeal.ID(1).getText()
            return f"{obj_name}.{field_name}"
            
        elif var_ctx.getChildCount() > 1 and var_ctx.getChild(1).getText() == '[':
            # Индексированная переменная: arr[index]
            obj_name = var_ctx.ID().getText()
            index_expr = self._compile_expression(var_ctx.expression(0))
            return f"{obj_name}[{index_expr}]"
        else:
            return "None"
    
    def _compile_function_call(self, ctx) -> str:
        try:
            func_name = ctx.ID().getText()
            
            # Компилируем аргументы
            args = []
            if ctx.argumentList():
                for expr in ctx.argumentList().expression():
                    args.append(self._compile_expression(expr))
            
            args_str = ", ".join(args)
            arg_count = len(args)
            
            # Определяем, какая версия функции должна быть вызвана
            if func_name in self.function_counter:
                # Ищем подходящую версию
                if arg_count in self.function_counter[func_name]['versions']:
                    actual_func_name = self.function_counter[func_name]['versions'][arg_count]
                else:
                    # Используем версию с соответствующим количеством аргументов
                    actual_func_name = f"{func_name}_{arg_count}arg"
            else:
                actual_func_name = func_name
            
            # Специальная обработка встроенных функций
            if func_name == 'write':
                return f"write({args_str})"
            elif func_name == 'read':
                if args:
                    return f"read({args_str})"
                else:
                    return "read()"
            elif func_name == 'range':
                return f"list(range({args_str}))"
            else:
                return f"{actual_func_name}({args_str})"
        except Exception as e:
            print(f"Ошибка компиляции вызова функции: {e}")
            return "None"
    
    def _compile_method_call(self, method_appeal_ctx) -> str:
        """Компилирует вызов метода класса"""
        obj_name = method_appeal_ctx.ID(0).getText()
        method_name = method_appeal_ctx.ID(1).getText()
        
        # Компилируем аргументы
        args = []
        if method_appeal_ctx.argumentList():
            for expr in method_appeal_ctx.argumentList().expression():
                args.append(self._compile_expression(expr))
        
        args_str = ", ".join(args) if args else ""
        return f"{obj_name}.{method_name}({args_str})"
    
    def _compile_literal(self, literal_ctx) -> str:
        try:
            if isinstance(literal_ctx, vecmatlangParser.IntLiteralContext):
                return literal_ctx.getText()
            elif isinstance(literal_ctx, vecmatlangParser.FloatLiteralContext):
                return literal_ctx.getText()
            elif isinstance(literal_ctx, vecmatlangParser.StringLiteralContext):
                # Сохраняем строку как есть - Python 3 по умолчанию использует UTF-8
                return literal_ctx.getText()
            elif isinstance(literal_ctx, vecmatlangParser.VectorLiteralContext):
                # Векторный литерал: [1, 2, 3]
                elements = []
                if literal_ctx.argumentList():
                    for expr in literal_ctx.argumentList().expression():
                        elements.append(self._compile_expression(expr))
                
                elements_str = ", ".join(elements)
                return f"np.array([{elements_str}], dtype=np.float64)"
            elif isinstance(literal_ctx, vecmatlangParser.MatrixLiteralContext):
                # Матричный литерал: [[1, 2], [3, 4]]
                rows = []
                
                # Проходим по всем дочерним элементам
                for i in range(literal_ctx.getChildCount()):
                    child = literal_ctx.getChild(i)
                    if isinstance(child, vecmatlangParser.ArgumentListContext):
                        # Это строка матрицы
                        row_elements = []
                        for expr in child.expression():
                            row_elements.append(self._compile_expression(expr))
                        rows.append(f"[{', '.join(row_elements)}]")
                
                if rows:
                    # Правильное создание матрицы numpy
                    return f"np.array([{', '.join(rows)}], dtype=np.float64)"
                else:
                    return "np.array([[]], dtype=np.float64)"
                
            return "None"
        except Exception as e:
            print(f"Ошибка компиляции литерала: {e}")
            import traceback
            traceback.print_exc()
            return "None"
    
    # ========== Обработка операторов управления ==========
    
    def enterIfStatement(self, ctx: vecmatlangParser.IfStatementContext):

        condition = self._compile_expression(ctx.expression())
        # Убираем лишние скобки из условия
        condition_clean = condition.strip()
        if condition_clean.startswith('(') and condition_clean.endswith(')'):
            condition_clean = condition_clean[1:-1].strip()

        print(f'DEBUG: Enter in ifStatement {ctx.getText()}')
        
        self._add_line(f"if {condition_clean}:")
        print(f'DEBUG: result: ({self.indent_level}) if {condition_clean}:')
        self.indent_level += 1
        self._in_if_block = True
    
    def exitIfStatement(self, ctx: vecmatlangParser.IfStatementContext):
        # Выходим из if блока только если не было else
        if hasattr(self, '_in_if_block') and self._in_if_block and not ctx.ELSE():
            self.indent_level -= 1
            self._in_if_block = False

        # Обработка else
        if ctx.ELSE():
            self.indent_level -= 1  # Выходим из if блока
            self._in_if_block = False
            self._add_line("else:")
            print(f'DEBUG: result: ({self.indent_level}) else:')
            self.indent_level += 1
            self._in_else_block = True

        print('DEBUG: Exit from ifStatement')
    
    def enterBlock(self, ctx: vecmatlangParser.BlockContext):
        # Блок уже обрабатывается через enterIfStatement и т.д.
        pass
    
    def exitBlock(self, ctx: vecmatlangParser.BlockContext):
        # Выходим из блока (if/else/for/while)
        if hasattr(self, '_in_if_block') and self._in_if_block:
            self.indent_level -= 1
            self._in_if_block = False
        elif hasattr(self, '_in_else_block') and self._in_else_block:
            self.indent_level -= 1
            self._in_else_block = False
    
    def enterForStatement(self, ctx: vecmatlangParser.ForStatementContext):
        var_name = ctx.ID().getText()
        
        print(f'DEBUG: Enter in forStatement {ctx.getText()}')

        # Компилируем аргументы range
        args = []
        if ctx.expression():
            for expr in ctx.expression():
                args.append(self._compile_expression(expr))
        
        args_str = ", ".join(args) if args else ""
        
        self._add_line(f"for {var_name} in range({args_str}):")
        print(f'DEBUG: result: ({self.indent_level}) for {var_name} in range({args_str}):')

        self.indent_level += 1
        self.loop_stack.append("for")
        self.local_vars.add(var_name)
    
    def exitForStatement(self, ctx: vecmatlangParser.ForStatementContext):
        if self.loop_stack and self.loop_stack[-1] == "for":
            self.loop_stack.pop()
        self.indent_level -= 1

        print('DEBUG: Exit from forStatement')
    
    def enterWhileStatement(self, ctx: vecmatlangParser.WhileStatementContext):
        condition = self._compile_expression(ctx.expression())
        condition_clean = condition.strip()
        if condition_clean.startswith('(') and condition_clean.endswith(')'):
            condition_clean = condition_clean[1:-1].strip()

        print(f'DEBUG: Enter in whileStatement {ctx.getText()}')
        
        self._add_line(f"while {condition_clean}:")
        print(f'DEBUG: result: ({self.indent_level}) while {condition_clean}:')
        self.indent_level += 1
        self.loop_stack.append("while")
    
    def exitWhileStatement(self, ctx: vecmatlangParser.WhileStatementContext):
        if self.loop_stack and self.loop_stack[-1] == "while":
            self.loop_stack.pop()
        self.indent_level -= 1

        print('DEBUG: Exit from whileStatement')

    def enterUntilStatement(self, ctx: vecmatlangParser.UntilStatementContext):
        condition = self._compile_expression(ctx.expression())
        condition_clean = condition.strip()
        if condition_clean.startswith('(') and condition_clean.endswith(')'):
            condition_clean = condition_clean[1:-1].strip()
        
        print(f'DEBUG: Enter in untilStatement {ctx.getText()}')

        # until выполняется ДО ТЕХ ПОР, ПОКА условие НЕ выполнится
        # то есть: while not (condition)
        self._add_line(f"while not ({condition_clean}):")
        print(f'DEBUG: result: ({self.indent_level}) while not ({condition_clean}):')
        self.indent_level += 1
        self.loop_stack.append("until")

    def exitUntilStatement(self, ctx: vecmatlangParser.UntilStatementContext):
        if self.loop_stack and self.loop_stack[-1] == "until":
            self.loop_stack.pop()
        self.indent_level -= 1

        print('DEBUG: Exit from untilStatement')
    
    def enterReturnStatement(self, ctx: vecmatlangParser.ReturnStatementContext):
        if ctx.argumentList():
            args = []
            for expr in ctx.argumentList().expression():
                args.append(self._compile_expression(expr))
            
            if len(args) > 1:
                # Возврат кортежа
                args_str = ", ".join(args)
                self._add_line(f"return {args_str}")
                print(f'DEBUG: result: ({self.indent_level}) return {args_str}')
            else:
                args_str = args[0] if args else ""
                self._add_line(f"return {args_str}")
                print(f'DEBUG: result: ({self.indent_level}) return {args_str}')
        else:
            self._add_line("return None")
            print(f'DEBUG: result: ({self.indent_level}) return None')
    
    def enterWriteStatement(self, ctx: vecmatlangParser.WriteStatementContext):
        args = []
        if ctx.argumentList():
            for expr in ctx.argumentList().expression():
                args.append(self._compile_expression(expr))
        
        args_str = ", ".join(args) if args else ""
        self._add_line(f"write({args_str})")
        print(f'DEBUG: result: ({self.indent_level}) write({args_str})')
    
    def enterReadStatement(self, ctx: vecmatlangParser.ReadStatementContext):
        # Этот метод не должен ничего добавлять в вывод
        # Чтение обрабатывается только когда используется как выражение
        pass
    
    # Обработка CONTINUE и BREAK
    def enterStatement(self, ctx: vecmatlangParser.StatementContext):
        # Проверяем, является ли это CONTINUE или BREAK
        if ctx.CONTINUE():
            if self.loop_stack:
                self._add_line("continue")
                print(f'DEBUG: result: ({self.indent_level}) continue')
        elif ctx.BREAK():
            if self.loop_stack:
                self._add_line("break")
                print(f'DEBUG: result: ({self.indent_level}) break')
    
    # ========== Генерация кода ==========
    
    def get_code(self) -> str:
        return "\n".join(self.output)