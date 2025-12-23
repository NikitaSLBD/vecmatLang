# main.py
import traceback

from antlr4 import *
from generated.vecmatlangParser import vecmatlangParser
from indentation_lexer import IndentationLexer, vecmatlangLexer
from syntaxerror_listener import SyntaxErrorListener, ErrorListener


EXAMPLES_DIR = 'examples/'

EXAMPLES_NAMES = [
    'example1.vml',
    'example2.vml',
    'example3.vml',
    'wrongsyntax_example1.vml',
    'wrongsyntax_example2.vml',
]

def read_vml(file_path: str) -> str | None:
    try:
        with open(file_path, 'r') as vml: return vml.read()
    except Exception as e: 
        print(f'Ошибка чтения файла {file_path}: {e}')


def get_analyze_tools(code: str) -> tuple[vecmatlangLexer, vecmatlangParser, ErrorListener]:

    # создаем потоки входа и токенов вместе с лексером и парсером
    stream = InputStream(code)
    lexer = IndentationLexer(stream) # кастомный лексер для обработки неявного блочного оператора 
    tokens_stream = CommonTokenStream(lexer)
    parser = vecmatlangParser(tokens_stream)

    # добавляем свой слушатель ошибок в лексер и парсер и удаляем слушатель ошибок по умолчанию
    error_listener = SyntaxErrorListener() # кастомный слушатель ошибок для лучшего контроля их вывода
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    return lexer, parser, error_listener

def analyze(file_path: str):

    code = read_vml(file_path)

    if not code: print('Анализ провален из-за ошибки чтения файла, возможно файл примера пустой')

    lexer, parser, error_listener = get_analyze_tools(code)
    
    try:

        tree = parser.program()

        error_count = error_listener.get_error_count()
        
        if not error_count:
            print(f"Анализ {file_path} завершен успешно. Синтаксических ошибок не обнаружено.")
        else:
            error_listener.print_errors()
            print(f"\nАнализ {file_path} завершен успешно. Обнаружены синтаксические ошибки.")

    except Exception as e: 

        print(f'Неизвестная ошибка при анализе {file_path}: {e}')
        print('Traceback:')
        traceback.print_exc()
        

if __name__ == "__main__":

    pathes = [EXAMPLES_DIR + file_name for file_name in EXAMPLES_NAMES]

    for file_path in pathes: 

        print(f'Начало анализа {file_path}')
        analyze(file_path)