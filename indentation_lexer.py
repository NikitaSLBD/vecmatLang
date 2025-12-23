from antlr4 import *
from antlr4.Token import CommonToken, Token
from generated.vecmatlangLexer import vecmatlangLexer

class IndentationLexer(vecmatlangLexer):
    def __init__(self, input=None):
        super().__init__(input)
        self.indent_stack = [0]  # стек уровней отступов
        self.tokens_queue = []   # очередь токенов для выдачи
        self.last_token = None
        self.at_start_of_line = True
        
    def nextToken(self):
        # Если есть токены в очереди, возвращаем их
        if self.tokens_queue:
            return self.tokens_queue.pop(0)
        
        # Получаем следующий токен
        token = super().nextToken()
        
        # Сохраняем последний токен (для отладки)
        self.last_token = token
        
        # Обработка EOF
        if token.type == Token.EOF:
            # В конце файла добавляем DEDENT для всех уровней отступа
            while len(self.indent_stack) > 1:
                dedent_token = self._create_token(
                    vecmatlangLexer.DEDENT, 
                    "<<DEDENT>>",
                    token.line,
                    1
                )
                self.tokens_queue.append(dedent_token)
                self.indent_stack.pop()
            
            self.tokens_queue.append(token)
            return self.tokens_queue.pop(0)
        
        # Если это NEWLINE, следующая строка начинается
        if token.type == vecmatlangLexer.NEWLINE:
            self.at_start_of_line = True
            return token
        
        # Если мы в начале строки и это не пробелы/табуляции
        if self.at_start_of_line and token.type not in [
            vecmatlangLexer.WS, 
            vecmatlangLexer.TAB, 
            vecmatlangLexer.COMMENT,
            vecmatlangLexer.NEWLINE
        ]:
            self.at_start_of_line = False
            
            # Подсчитываем отступ текущей строки
            current_indent = self._calculate_indent(token)
            
            # Сравниваем с предыдущим отступом
            if current_indent > self.indent_stack[-1]:
                # Увеличиваем отступ - добавляем токен INDENT
                self.indent_stack.append(current_indent)
                indent_token = self._create_token(
                    vecmatlangLexer.INDENT,
                    "<<INDENT>>",
                    token.line,
                    1
                )
                self.tokens_queue.append(indent_token)
                self.tokens_queue.append(token)
                return self.tokens_queue.pop(0)
            
            elif current_indent < self.indent_stack[-1]:
                # Уменьшаем отступ - добавляем токены DEDENT
                while current_indent < self.indent_stack[-1]:
                    self.indent_stack.pop()
                    dedent_token = self._create_token(
                        vecmatlangLexer.DEDENT,
                        "<<DEDENT>>",
                        token.line,
                        1
                    )
                    self.tokens_queue.append(dedent_token)
                
                self.tokens_queue.append(token)
                return self.tokens_queue.pop(0)
        
        return token
    
    def _calculate_indent(self, token):
        """Вычисляет отступ текущей строки"""
        # Получаем текущую позицию в потоке
        current_pos = self._input.index
        
        try:
            # Получаем весь текст
            self._input.seek(0)
            text = self._input._data if hasattr(self._input, '_data') else str(self._input)
            
            # Находим начало текущей строки
            line_start = current_pos
            while line_start > 0 and line_start <= len(text) and text[line_start-1] != '\n':
                line_start -= 1
            
            # Подсчитываем отступ от начала строки
            indent = 0
            i = line_start
            while i < len(text) and i < current_pos:
                if i >= len(text):
                    break
                if text[i] == ' ':
                    indent += 1
                elif text[i] == '\t':
                    indent += 4  # табуляция = 4 пробела
                else:
                    break
                i += 1
            
            # Возвращаем каретку на место
            self._input.seek(current_pos)
            return indent
            
        except Exception as e:
            # Если возникла ошибка, возвращаем отступ 0
            print(f"Ошибка при вычислении отступа: {e}")
            return 0
    
    def _create_token(self, token_type, text, line, column):
        """Создает токен правильно"""
        # Получаем source из текущего токена
        source = None
        if self.last_token:
            source = self.last_token.source if hasattr(self.last_token, 'source') else None
        
        # Создаем токен
        token = CommonToken(
            source=source,
            type=token_type,
            channel=Token.DEFAULT_CHANNEL,
            start=-1,
            stop=-1
        )
        token.text = text
        token.line = line
        token.column = column
        return token