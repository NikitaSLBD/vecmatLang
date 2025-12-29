# compiler.py
import sys
import os
import traceback
import py_compile
from typing import List, Tuple

from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker

from syntaxerror_listener import SyntaxErrorListener
from syntax_analyzer import read_vml, get_analyze_tools, EXAMPLES_DIR
from semantic_analyzer import SemanticAnalyzer
from python_compiler import PythonCompiler

COMPILED_CODE_DIR = 'compiled/'


class Compiler:
    def __init__(self):
        self.semantic_analyzer = None
        self.python_compiler = None
    
    def compile(self, source_code: str, output_file: str = None) -> Tuple[bool, str, List[str]]:
        """Компилирует код VML в Python байт-код"""
        
        try:
            print("Шаг 1: Синтаксический анализ...")
            # 1. Синтаксический анализ
            _, parser, error_listener = get_analyze_tools(source_code, SyntaxErrorListener())
            tree = parser.program()
            
            if error_listener.get_error_count() > 0:
                errors = [f"Синтаксическая ошибка: {e['msg']} (строка {e['line']})" 
                         for e in error_listener.get_errors()]
                return False, None, errors
            
            print("Синтаксический анализ завершен")
            
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
        output_path = os.path.join(COMPILED_CODE_DIR, example_file).replace('.vml', '.pyc')
        
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
                    print(f" {warning}")
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