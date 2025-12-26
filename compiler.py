# compiler.py

import sys
import os
import traceback
import marshal
import py_compile
from enum import Enum
from typing import Dict, List, Optional, Tuple, Any

from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker
from generated.vecmatlangParser import vecmatlangParser
from generated.vecmatlangListener import vecmatlangListener

from syntaxerror_listener import SyntaxErrorListener
from syntax_analyzer import read_vml, get_analyze_tools, EXAMPLES_DIR
from semantic_analyzer import SemanticAnalyzer, Type, FunctionSymbol, ClassSymbol

COMPILED_CODE_DIR = 'compiled/'


class PythonCompiler(vecmatlangListener):
    def __init__(self):
        super().__init__()
        self.output = []
        self.indent_level = 0
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
        # Добавляем импорты
        self._add_raw_line("import numpy as np")
        self._add_raw_line("import sys")
        self._add_raw_line("import math")
        self._add_raw_line("")
        
        # Добавляем встроенные функции
        self._add_raw_line("# ========== Встроенные функции ==========")
        self._add_raw_line("def _vml_write(*args):")
        self._add_raw_line("    for arg in args:")
        self._add_raw_line("        sys.stdout.write(str(arg))")
        self._add_raw_line("    sys.stdout.write('\\n')")
        self._add_raw_line("    sys.stdout.flush()")
        self._add_raw_line("")
        
        self._add_raw_line("def _vml_read(prompt=''):")
        self._add_raw_line("    if prompt:")
        self._add_raw_line("        sys.stdout.write(prompt)")
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
    
    # ========== Обработка функций ==========
    
    def enterFunctionDecl(self, ctx: vecmatlangParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        
        # Получаем параметры
        params = []
        if ctx.parameterList():
            for param in ctx.parameterList().ID():
                params.append(param.getText())
        
        # Начинаем определение функции
        self.current_function = func_name
        self.function_params = params
        self.local_vars = set(params)
        
        param_str = ", ".join(params)
        self._add_line(f"def {func_name}({param_str}):")
        self.indent_level += 1
    
    def exitFunctionDecl(self, ctx: vecmatlangParser.FunctionDeclContext):
        if self.current_function:
            # Если функция не имеет return, добавляем неявный возврат None
            if self.output and not any(line.strip().startswith("return") for line in self.output[-5:]):
                self._add_line("return None")
            
            self.current_function = None
            self.function_params = []
            self.indent_level -= 1
            self._add_raw_line("")
    
    # ========== Обработка классов ==========
    
    def enterClassDecl(self, ctx: vecmatlangParser.ClassDeclContext):
        class_name = ctx.ID().getText()
        
        # Получаем параметры конструктора
        params = []
        if ctx.parameterList():
            for param in ctx.parameterList().ID():
                params.append(param.getText())
        
        self.current_class = class_name
        self.in_class_body = False
        self.in_class_init = True
        self.class_fields = set(params)  # Параметры конструктора тоже становятся полями
        
        # Определяем конструктор
        param_str = ", ".join(["self"] + params)
        self._add_line(f"class {class_name}:")
        self.indent_level += 1
        self._add_line(f"def __init__({param_str}):")
        self.indent_level += 1
        
        # Сохраняем параметры как поля
        for param in params:
            self._add_line(f"self.{param} = {param}")
        
        # Флаг, что мы в теле класса (после __init__)
        self.in_class_body = True
    
    def exitClassDecl(self, ctx: vecmatlangParser.ClassDeclContext):
        if self.current_class:
            # Выходим из __init__
            self.indent_level -= 1
            self.in_class_init = False
            
            # Выходим из класса
            self.indent_level -= 1
            self.current_class = None
            self.in_class_body = False
            self._add_raw_line("")
    
    def enterClassBody(self, ctx: vecmatlangParser.ClassBodyContext):
        # Теперь мы внутри тела класса (после __init__)
        self.in_class_body = True
    
    def exitClassBody(self, ctx: vecmatlangParser.ClassBodyContext):
        self.in_class_body = False
    
    # ========== Обработка методов ==========
    
    def enterMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        if not self.current_class:
            return
        
        method_name = ctx.ID().getText()
        
        # Получаем параметры
        params = []
        if ctx.parameterList():
            for param in ctx.parameterList().ID():
                params.append(param.getText())
        
        self.current_method = True
        self.current_function = method_name
        self.function_params = params
        self.local_vars = set(["self"] + params)
        
        param_str = ", ".join(["self"] + params)
        self._add_line(f"def {method_name}({param_str}):")
        self.indent_level += 1
    
    def exitMethodDecl(self, ctx: vecmatlangParser.MethodDeclContext):
        if self.current_method:
            # Если метод не имеет return, добавляем неявный возврат None
            if self.output and not any(line.strip().startswith("return") for line in self.output[-5:]):
                self._add_line("return None")
            
            self.current_method = False
            self.current_function = None
            self.function_params = []
            self.indent_level -= 1
    
    # ========== Обработка присваиваний ==========
    
    def enterSingleAssignment(self, ctx: vecmatlangParser.SingleAssignmentContext):
        var_ctx = ctx.var()
        expr_ctx = ctx.expression()
        
        # Компилируем выражение
        expr_code = self._compile_expression(expr_ctx)
        
        # Получаем имя переменной
        if var_ctx.ID():
            var_name = var_ctx.ID().getText()
            
            # Проверяем контекст
            if self.in_class_init:
                # В конструкторе класса
                self.class_fields.add(var_name)
                self._add_line(f"self.{var_name} = {expr_code}")
            elif self.current_method and var_name not in self.function_params:
                # В методе класса
                if var_name in self.class_fields:
                    # Если это поле класса, используем self.
                    self._add_line(f"self.{var_name} = {expr_code}")
                else:
                    # Локальная переменная в методе
                    self.local_vars.add(var_name)
                    self._add_line(f"{var_name} = {expr_code}")
            else:
                # Глобальная или локальная переменная в функции
                self.local_vars.add(var_name)
                self._add_line(f"{var_name} = {expr_code}")
                
        elif var_ctx.fieldAppeal():
            # Обращение к полю объекта: obj.field = expr
            field_appeal = var_ctx.fieldAppeal()
            obj_name = field_appeal.ID(0).getText()
            field_name = field_appeal.ID(1).getText()
            self._add_line(f"{obj_name}.{field_name} = {expr_code}")
    
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
        op = ctx.getChild(1).getText()
        
        # Специальная обработка операций
        if op == '*':
            # Для умножения используем специальные функции для векторов/матриц
            if self._is_likely_vector_or_matrix(left) or self._is_likely_vector_or_matrix(right):
                if self._is_likely_matrix(left) or self._is_likely_matrix(right):
                    return f"_vml_matrix_mult({left}, {right})"
                else:
                    return f"_vml_vector_mult({left}, {right})"
        
        # Логические операции
        if op == '&&':
            op = 'and'
        elif op == '||':
            op = 'or'
        
        return f"({left} {op} {right})"
    
    def _is_likely_vector_or_matrix(self, expr_code: str) -> bool:
        """Проверяет, вероятно ли выражение является вектором или матрицей"""
        if not expr_code:
            return False
        expr_lower = expr_code.lower()
        vector_indicators = ['[', 'np.array', 'vector', 'v1', 'v2', 'vec', 'sum_v', 'prod_m']
        return any(indicator in expr_lower for indicator in vector_indicators)
    
    def _is_likely_matrix(self, expr_code: str) -> bool:
        """Проверяет, вероятно ли выражение является матрицей"""
        if not expr_code:
            return False
        expr_lower = expr_code.lower()
        matrix_indicators = ['[[', 'matrix', 'm1', 'm2']
        return any(indicator in expr_lower for indicator in matrix_indicators)
    
    def _compile_primary_expression(self, ctx) -> str:
        try:
            if isinstance(ctx, vecmatlangParser.VarExprContext):
                var_ctx = ctx.var()
                
                if var_ctx.fieldAppeal():
                    # Обращение к полю класса: obj.field
                    field_appeal = var_ctx.fieldAppeal()
                    obj_name = field_appeal.ID(0).getText()
                    field_name = field_appeal.ID(1).getText()
                    return f"{obj_name}.{field_name}"
                    
                elif var_ctx.ID():
                    var_name = var_ctx.ID().getText()
                    
                    # Проверяем, является ли это полем класса
                    if self.current_method and var_name in self.class_fields:
                        return f"self.{var_name}"
                    else:
                        return var_name
                        
                elif var_ctx.getChildCount() > 1 and var_ctx.getChild(1).getText() == '[':
                    # Индексированная переменная
                    obj_name = var_ctx.ID().getText()
                    index_expr = self._compile_expression(var_ctx.expression(0))
                    return f"{obj_name}[{index_expr}]"
                    
            elif isinstance(ctx, vecmatlangParser.ParenExprContext):
                inner = self._compile_expression(ctx.expression())
                return f"({inner})"
                
            elif isinstance(ctx, vecmatlangParser.FuncCallExprContext):
                return self._compile_function_call(ctx)
                
            elif isinstance(ctx, vecmatlangParser.FieldExprContext):
                field_appeal = ctx.fieldAppeal()
                obj_name = field_appeal.ID(0).getText()
                field_name = field_appeal.ID(1).getText()
                return f"{obj_name}.{field_name}"
                
            elif isinstance(ctx, vecmatlangParser.MethodExprContext):
                method_appeal = ctx.methodAppeal()
                obj_name = method_appeal.ID(0).getText()
                method_name = method_appeal.ID(1).getText()
                
                # Компилируем аргументы
                args = []
                if method_appeal.argumentList():
                    for expr in method_appeal.argumentList().expression():
                        args.append(self._compile_expression(expr))
                
                args_str = ", ".join(args) if args else ""
                return f"{obj_name}.{method_name}({args_str})"
                
            elif isinstance(ctx, vecmatlangParser.LiteralExprContext):
                return self._compile_literal(ctx.literal())
                
            elif isinstance(ctx, vecmatlangParser.TypeExprContext):
                # Конструктор типа: int(x), float(x), vector([...]), matrix([[...]])
                type_ctx = ctx.type_()
                type_name = type_ctx.getText()
                
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
                # Проверяем, не является ли это конструктором класса
                if func_name[0].isupper():  # Имена классов обычно с заглавной буквы
                    return f"{func_name}({args_str})"
                else:
                    return f"{func_name}({args_str})"
        except Exception as e:
            print(f"Ошибка компиляции вызова функции: {e}")
            return "None"
    
    def _compile_literal(self, ctx) -> str:
        try:
            if isinstance(ctx, vecmatlangParser.IntLiteralContext):
                return ctx.getText()
            elif isinstance(ctx, vecmatlangParser.FloatLiteralContext):
                return ctx.getText()
            elif isinstance(ctx, vecmatlangParser.StringLiteralContext):
                return ctx.getText()
            elif isinstance(ctx, vecmatlangParser.VectorLiteralContext):
                # Векторный литерал: [1, 2, 3]
                elements = []
                if ctx.expression():
                    for expr in ctx.expression():
                        elements.append(self._compile_expression(expr))
                
                elements_str = ", ".join(elements)
                return f"np.array([{elements_str}], dtype=np.float64)"
            elif isinstance(ctx, vecmatlangParser.MatrixLiteralContext):
                # Матричный литерал: [[1, 2], [3, 4]]
                # Собираем все элементы
                rows = []
                current_row = []
                
                for i in range(ctx.getChildCount()):
                    child = ctx.getChild(i)
                    if isinstance(child, vecmatlangParser.ExpressionContext):
                        current_row.append(self._compile_expression(child))
                    elif child.getText() == ']' and current_row:
                        rows.append(f"[{', '.join(current_row)}]")
                        current_row = []
                
                if rows:
                    return f"np.array([{', '.join(rows)}], dtype=np.float64)"
                else:
                    return "np.array([[]], dtype=np.float64)"
            
            return "None"
        except Exception as e:
            print(f"Ошибка компиляции литерала: {e}")
            return "None"
    
    # ========== Обработка операторов управления ==========
    
    def enterIfStatement(self, ctx: vecmatlangParser.IfStatementContext):
        condition = self._compile_expression(ctx.expression())
        self._add_line(f"if {condition}:")
        self.indent_level += 1
    
    def exitIfStatement(self, ctx: vecmatlangParser.IfStatementContext):
        # Выходим из if блока
        self.indent_level -= 1
        
        # Обработка else
        if ctx.ELSE():
            self._add_line("else:")
            self.indent_level += 1
    
    def enterForStatement(self, ctx: vecmatlangParser.ForStatementContext):
        var_name = ctx.ID().getText()
        
        # Компилируем аргументы range
        args = []
        if ctx.expression():
            for expr in ctx.expression():
                args.append(self._compile_expression(expr))
        
        args_str = ", ".join(args) if args else ""
        
        self._add_line(f"for {var_name} in range({args_str}):")
        self.indent_level += 1
        self.loop_stack.append("for")
        self.local_vars.add(var_name)
    
    def exitForStatement(self, ctx: vecmatlangParser.ForStatementContext):
        if self.loop_stack and self.loop_stack[-1] == "for":
            self.loop_stack.pop()
        self.indent_level -= 1
    
    def enterWhileStatement(self, ctx: vecmatlangParser.WhileStatementContext):
        condition = self._compile_expression(ctx.expression())
        self._add_line(f"while {condition}:")
        self.indent_level += 1
        self.loop_stack.append("while")
    
    def exitWhileStatement(self, ctx: vecmatlangParser.WhileStatementContext):
        if self.loop_stack and self.loop_stack[-1] == "while":
            self.loop_stack.pop()
        self.indent_level -= 1
    
    def enterUntilStatement(self, ctx: vecmatlangParser.UntilStatementContext):
        condition = self._compile_expression(ctx.expression())
        self._add_line(f"while not ({condition}):")
        self.indent_level += 1
        self.loop_stack.append("until")
    
    def exitUntilStatement(self, ctx: vecmatlangParser.UntilStatementContext):
        if self.loop_stack and self.loop_stack[-1] == "until":
            self.loop_stack.pop()
        self.indent_level -= 1
    
    def enterReturnStatement(self, ctx: vecmatlangParser.ReturnStatementContext):
        if ctx.argumentList():
            args = []
            for expr in ctx.argumentList().expression():
                args.append(self._compile_expression(expr))
            
            if len(args) > 1:
                # Возврат кортежа
                args_str = ", ".join(args)
                self._add_line(f"return ({args_str},)")
            else:
                args_str = args[0] if args else ""
                self._add_line(f"return {args_str}")
        else:
            self._add_line("return None")
    
    def enterWriteStatement(self, ctx: vecmatlangParser.WriteStatementContext):
        args = []
        if ctx.argumentList():
            for expr in ctx.argumentList().expression():
                args.append(self._compile_expression(expr))
        
        args_str = ", ".join(args) if args else ""
        self._add_line(f"write({args_str})")
    
    def enterReadStatement(self, ctx: vecmatlangParser.ReadStatementContext):
        args = []
        if ctx.argumentList():
            for expr in ctx.argumentList().expression():
                args.append(self._compile_expression(expr))
        
        if args:
            self._add_line(f"read({args[0]})")
        else:
            self._add_line("read()")
    
    # Обработка CONTINUE и BREAK
    def enterStatement(self, ctx: vecmatlangParser.StatementContext):
        # Проверяем, является ли это CONTINUE или BREAK
        if ctx.CONTINUE():
            if self.loop_stack:
                self._add_line("continue")
        elif ctx.BREAK():
            if self.loop_stack:
                self._add_line("break")
    
    # ========== Генерация кода ==========
    
    def get_code(self) -> str:
        return "\n".join(self.output)


class Compiler:
    def __init__(self):
        self.semantic_analyzer = None
        self.python_compiler = None
    
    def compile(self, source_code: str, output_file: str = None) -> Tuple[bool, str, List[str]]:
        """Компилирует код VML в Python байт-код"""
        
        try:
            print("Шаг 1: Синтаксический анализ...")
            # 1. Синтаксический анализ
            lexer, parser, error_listener = get_analyze_tools(source_code, SyntaxErrorListener())
            tree = parser.program()
            
            if error_listener.get_error_count() > 0:
                errors = [f"Синтаксическая ошибка: {e['msg']} (строка {e['line']})" 
                         for e in error_listener.get_errors()]
                return False, None, errors
            
            print(" Синтаксический анализ завершен")
            
            print("Шаг 2: Семантический анализ...")
            # 2. Семантический анализ
            walker = ParseTreeWalker()
            self.semantic_analyzer = SemanticAnalyzer()
            walker.walk(self.semantic_analyzer, tree)
            
            if self.semantic_analyzer.errors:
                print(f" Найдены семантические ошибки: {len(self.semantic_analyzer.errors)}")
                return False, None, self.semantic_analyzer.errors
            
            print(" Семантический анализ завершен")
            
            print("Шаг 3: Компиляция в Python...")
            # 3. Компиляция в Python
            self.python_compiler = PythonCompiler()
            walker.walk(self.python_compiler, tree)
            
            python_code = self.python_compiler.get_code()
            
            print(" Компиляция в Python завершена")
            
            # 4. Генерация байт-кода
            if output_file:
                if not output_file.endswith('.pyc'):
                    output_file += '.pyc'
                
                # Создаем временный Python файл
                temp_py_file = output_file.replace('.pyc', '.py')
                with open(temp_py_file, 'w', encoding='utf-8') as f:
                    f.write(python_code)
                
                print(f"Создан временный файл: {temp_py_file}")
                
                # Компилируем в байт-код
                py_compile.compile(temp_py_file, cfile=output_file)
                
                print(f"Создан байт-код: {output_file}")
                
                # Удаляем временный файл
                os.remove(temp_py_file)
                print("Временный файл удален")
                
                return True, output_file, self.semantic_analyzer.warnings
            
            return True, python_code, self.semantic_analyzer.warnings
            
        except Exception as e:
            error_msg = f"Ошибка компиляции: {str(e)}\n{traceback.format_exc()}"
            print(f" Критическая ошибка: {e}")
            return False, None, [error_msg]
    
    def compile_file(self, input_file: str, output_file: str = None) -> Tuple[bool, str, List[str]]:
        """Компилирует файл VML в Python байт-код"""
        
        try:
            print(f"Чтение файла: {input_file}")
            source_code = read_vml(input_file)
            if not source_code:
                return False, None, ["Ошибка чтения файла"]
            
            print(f"Размер исходного кода: {len(source_code)} символов")
            
            if not output_file:
                output_file = input_file.replace('.vml', '.pyc')
            
            return self.compile(source_code, output_file)
            
        except Exception as e:
            error_msg = f"Ошибка компиляции файла: {str(e)}"
            print(f" Ошибка: {e}")
            return False, None, [error_msg]


def compile_examples():
    """Компилирует примеры из задания"""
    
    examples = [
        ("example1.vml", "Пример 1: Одиночное присваивание и операции"),
        ("example2.vml", "Пример 2: Функции и циклы"),
        ("example3.vml", "Пример 3: Перегрузка функций"),
        ("example4.vml", "Пример 4: Классы и методы")
    ]
    
    compiler = Compiler()
    
    for example_file, description in examples:
        print(f"\n{'='*60}")
        print(f"{description}")
        print(f"{'='*60}")
        
        input_path = os.path.join(EXAMPLES_DIR, example_file)
        output_path = .replace('.vml', '.pyc')
        
        success, result, warnings = compiler.compile_file(input_path, output_path)
        
        if success:
            print(f" Успешно скомпилирован в: {result}")
            
            # Показываем сгенерированный Python код
            py_file = result.replace('.pyc', '.py')
            # Создаем файл для просмотра
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(compiler.python_compiler.get_code())
            
            print(f"\nСгенерированный Python код сохранен в: {py_file}")
            
            if warnings:
                print("\nПредупреждения:")
                for warning in warnings:
                    print(f"  • {warning}")
        else:
            print(f" Ошибка компиляции:")
            if result:
                if isinstance(result, list):
                    for i, error in enumerate(result, 1):
                        print(f"  {i}. {error}")
                else:
                    print(f"  • {result}")
            else:
                print(" Неизвестная ошибка")


def main():
    """Главная функция"""
    
    print("="*60)
    print("Компилятор VML в Python байт-код")
    print("="*60)
    
    if len(sys.argv) > 1:
        # Компиляция файла из аргументов командной строки
        compiler = Compiler()
        
        for input_file in sys.argv[1:]:
            if input_file.endswith('.vml'):
                print(f"\nКомпиляция {input_file}...")
                success, result, warnings = compiler.compile_file(input_file)
                
                if success:
                    print(f" Успешно: {result}")
                    if warnings:
                        print("Предупреждения:")
                        for warning in warnings:
                            print(f"  • {warning}")
                else:
                    print(" Ошибки:")
                    if isinstance(result, list):
                        for i, error in enumerate(result, 1):
                            print(f"  {i}. {error}")
                    else:
                        print(f" {result}")
            else:
                print(f"Пропущен файл (не .vml): {input_file}")
    else:
        # Интерактивный режим или компиляция примеров
        print("\nВыберите режим:")
        print("1. Компилировать примеры из задания")
        print("2. Ввести путь к файлу .vml")
        print("3. Выход")
        
        while True:
            choice = input("\nВведите номер (1-3): ").strip()
            
            if choice == "1":
                compile_examples()
                break
            elif choice == "2":
                file_path = input("Введите путь к файлу .vml: ").strip()
                if os.path.exists(file_path) and file_path.endswith('.vml'):
                    compiler = Compiler()
                    success, result, warnings = compiler.compile_file(file_path)
                    
                    if success:
                        print(f" Успешно скомпилирован в: {result}")
                        if warnings:
                            print("Предупреждения:")
                            for warning in warnings:
                                print(f"  • {warning}")
                    else:
                        print(" Ошибки:")
                        if isinstance(result, list):
                            for i, error in enumerate(result, 1):
                                print(f"  {i}. {error}")
                        else:
                            print(f"  • {result}")
                else:
                    print(f"Файл не найден или не имеет расширение .vml: {file_path}")
                break
            elif choice == "3":
                print("Выход...")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}")
        traceback.print_exc()