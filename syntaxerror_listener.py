from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.error_count = 0
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_info = {
            'line': line,
            'column': column + 1,
            'msg': msg,
            'offending_symbol': offendingSymbol.text if offendingSymbol else None
        }
        self.errors.append(error_info)
        self.error_count += 1
    
    def get_error_count(self):
        return self.error_count
    
    def get_errors(self):
        return self.errors
    
    def print_errors(self):
        if self.error_count == 0:
            print("Синтаксических ошибок не обнаружено.")
            return
        
        print(f"\nОбнаружено синтаксических ошибок: {self.error_count}")
        
        for i, error in enumerate(self.errors, 1):
            print(f"\nОшибка #{i}:")
            print(f"  Строка: {error['line']}, Колонка: {error['column']}")
            print(f"  Сообщение: {error['msg']}")
            if error['offending_symbol']:
                print(f"  Символ: '{error['offending_symbol']}'")