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
        self.pending_indent_check = False
        
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
            self.pending_indent_check = True
            return token

        # Если это комментарий
        if token.type == vecmatlangLexer.COMMENT:
            # Комментарий не должен влиять на отступы
            # Если мы в начале строки, пропускаем его и продолжаем
            if self.at_start_of_line:
                # Пропускаем комментарий и получаем следующий токен
                return self.nextToken()
            else:
                # Комментарий в середине строки - просто возвращаем
                return token

        # Если мы в начале строки (или ожидаем проверку отступа)
        if self.at_start_of_line or self.pending_indent_check:
            # Пропускаем пробелы и табы при подсчете отступов
            if token.type in [vecmatlangLexer.WS, vecmatlangLexer.TAB]:
                return token
            
            # Если это не пробельный токен, значит начало реального контента строки
            self.at_start_of_line = False
            self.pending_indent_check = False
            
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
            
            # Если отступ такой же, просто возвращаем токен
            return token

        return token
    
    def _calculate_indent(self, token):
        """Вычисляет отступ текущей строки на основе позиции токена"""
        # Самый простой способ: использовать position в токене
        # Проверяем, есть ли у токена информация о позиции
        if hasattr(token, 'column'):
            # column обычно 1-индексирован
            return max(0, token.column - 1)
        
        # Если нет column, пробуем вычислить из строки и индекса
        if hasattr(token, 'start') and token.start >= 0:
            try:
                # Получаем текст до этого токена
                input_str = self._input.strdata if hasattr(self._input, 'strdata') else str(self._input)
                
                # Находим начало строки
                start_pos = token.start
                line_start = start_pos
                while line_start > 0 and input_str[line_start-1] != '\n':
                    line_start -= 1
                
                # Подсчитываем отступ
                indent = 0
                pos = line_start
                while pos < start_pos and pos < len(input_str):
                    if input_str[pos] == ' ':
                        indent += 1
                    elif input_str[pos] == '\t':
                        indent += 4
                    elif input_str[pos] == '#':  # комментарий
                        # Игнорируем отступ после комментария
                        break
                    else:
                        break
                    pos += 1
                
                return indent
            except Exception as e:
                print(f"Ошибка при вычислении отступа: {e}")
        
        return 0
    
    def _create_token(self, token_type, text, line, column):
        """Создает токен правильно"""
        # Создаем токен
        token = CommonToken(
            type=token_type,
            channel=Token.DEFAULT_CHANNEL,
            start=-1,
            stop=-1
        )
        token.text = text
        token.line = line
        token.column = column
        return token