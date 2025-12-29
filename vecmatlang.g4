/*
Файл грамматики для vecmatLang 
vecmatLang - Язык для работы с векторами и матрицами
с поддержкой создания своих собственных структурных типов
основные особенности: 
* неявное объявление переменных
* множественное присваивание
* объявление функций только в начале программы
* перегрузка подпрограмм
* неявный блочный оператор (INDENT, DEDENT)
* объявление функций только в начале программы
* операторы цикла: for, while, until
* условный оператор if-then-else
* встроенные функции: read(), write(), len()
* векторное скалярное произведение и нахождеие нормы
* умножение матриц и нахождение нормы
* арифметические операции: +, -, *, /, || 
 */
grammar vecmatlang;

// Lexer (Основные токены языка)

// Невидимые токены 
WS: [ ]+ -> skip; // Токен пробелов (игнорируется)
NEWLINE: '\r'? '\n'; // Токен, обозначающий переход на новую строку
TAB: '\t' -> skip; // токен табуляции (игнорируется)

// Токены неявного блочного оператора
/* 
INDENT и DEDENT будут обрабатываться кастомным лексером indentation_lexer.py
только декларация для парсера
*/
INDENT: '<<INDENT>>'; 
DEDENT: '<<DEDENT>>';

// Токены ключевых слов языка
IF: 'if';
THEN: 'then';
ELSE: 'else';
FOR: 'for';
IN: 'in';
WHILE: 'while';
UNTIL: 'until';
FUNC: 'func';
RETURN: 'return';
WRITE: 'write';
READ: 'read';
RANGE: 'range';
CLASS: 'class';
METHOD: 'method';
CONTINUE: 'continue';
BREAK: 'break';
LEN: 'len';

// Токены логических операторов
AND: '&&'; // логическое И
OR: '||'; // логическое ИЛИ
NOT: '!'; // логическое отрицание

// Токены типов
/*
Нужны для реализации явного преобразования типов
такие токены существуют не для всех встроенных типов языка
а только для основных: целое, дробное, вектор, матрица
 */
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
VECTOR: 'vector';
MATRIX: 'matrix';

// Токены литералов
/*
показывают как различные атомарные конструкции представлены в языке
идентификатор: ghost56, целое: 67, дробное: 78.7, строка: "fgfhghg"
 */
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+;
STRING: '"' (~["\\\r\n] | '\\' ["\\])* '"';

COMMENT: '#' ~[\r\n]* -> skip; // Токен комментария в языке (игнорируется)



// Parser (Основные правила языка КС-грамматика)

// стартовое правило (корень синтаксического дерева)
/*
Программа может начинаться с пустых строк (NEWLINE*)
затем могут быть объявления классов (classDecl*)
после чего могут быть объявления функций (functionDecl*)
затем возможно идут различные statement блоки 
в конце обязательно должен быть знак конца файла (EOF)
 */
program: NEWLINE* classDecl* functionDecl* statement* EOF; 

// правило объявления функции
/*
Начинается с ключевого слова "func" (FUNC) 
после которого идет идентификатор функции (ID)
возможно, список параметров в скобках (parameterList?)
двоеточие, как знак окончания сигнатуры 
далее минимум один переход на новую строку (NEWLINE+)
в конце блок кода (block)
 */
functionDecl: FUNC ID '(' parameterList? ')' ':' NEWLINE+ block; 
parameterList: ID (',' ID)*; // правило, определяющие список параметров 

// Правило построения блока кода
/*
Использует токены неявного блочного оператора (INDENT, DEDENT)
между ними должен быть минимум один statement блок
 */
block: INDENT statement+ DEDENT;

// правило объявления класса
/*
Начинается с ключевого слова "class" (CLASS) 
после которого идет идентификатор класса (ID)
возможно, список параметров в скобках (parameterList?)
двоеточие, как знак окончания сигнатуры 
далее минимум один переход на новую строку (NEWLINE+)
в конце тело класса (сlassBody)
 */
classDecl: CLASS ID '(' parameterList? ')' ':' NEWLINE+ classBody;

// Правило описывающее тело класса
/*
Использует токены неявного блочного оператора (INDENT, DEDENT)
между ними должен быть минимум один statement блок либо объявления метода или функции
 */
classBody: INDENT (statement | methodDecl | functionDecl)+ DEDENT;

// правило объявления метода
/*
Начинается с ключевого слова "method" (METHOD) 
после которого идет идентификатор метода (ID)
возможно, список параметров в скобках (parameterList?)
двоеточие, как знак окончания сигнатуры 
далее минимум один переход на новую строку (NEWLINE+)
в конце блок кода (block)
 */
methodDecl: METHOD ID '(' parameterList? ')' ':' NEWLINE+ block;

// Токены обращенич к полям и методам класса
fieldAppeal: ID '.' ID;
methodAppeal: ID '.' ID '(' argumentList? ')';

// правило описывающее все главные конструкции языка (основные потомки корня в синтаксическом дереве)
statement
    : assignment NEWLINE? // присваивание  
    | ifStatement // условный оператор if-then-else 
    | forStatement // оператор цикла for
    | whileStatement // оператор цикла while
    | untilStatement // оператор цикла until
    | expression NEWLINE? // любое выражение 
    | returnStatement NEWLINE? // возрат значения из функции 
    | writeStatement NEWLINE?  // функция вывода write
    | readStatement NEWLINE? // функция ввода read
    | CONTINUE NEWLINE? // оператор управления continue
    | BREAK NEWLINE? // оператор управления break
    | NEWLINE // пустая строка
    ;

// правило описывающее переменную
var 
    : ID // обычная переменная 
    | fieldAppeal // переменная как поле класса
    | ID '[' expression ']' // индексированная переменная
    ;

// правило присваивания
assignment
    : singleAssignment // одиночное присваивание 
    | multipleAssignment // многоцелевое присваивание 
    ;

singleAssignment: var '=' expression; // правило построения одиночного присваивания 

// правило построения многоцелевого присваивания
/*
Перед оператором присваивания может быть перечисление переменных, минимум 2
после оператора присваивания может быть либо вызов функции (primaryExpression), либо список минимум из 2 выражений
 */
multipleAssignment: var (',' var)+ '=' (primaryExpression | expression (',' expression)+); 

// правило условного оператора if-then-else
/*
В начале ключевое слово "if" (IF)
затем любое логическое выражение (expression)
После этого ключевое слово "then" (THEN)
далее минимум один переход на новую строку (NEWLINE+)
после всего блок кода (block)
в конце возможно дополнительное ветвление ((ELSE NEWLINE+ block)?)
 */
ifStatement: 
    IF expression THEN NEWLINE+ 
    block
    (ELSE NEWLINE+ block)?;

// Правило оператора цикла 
/*
В начале ключевое слово "for" (FOR)
затем идетификатор переменной итератора цикла (ID)
после этого ключевое слово "in" (IN)
далее вызов функции range с одним, двумя или тремя аргументами 
в дальнейшем минимум один переход на новую строку (NEWLINE+)
в конце блок кода (block)
 */
forStatement: 
    FOR ID IN RANGE '(' expression (',' expression)? (',' expression)? ')' NEWLINE+
    block;

// Правило оператора цикла 
/*
В начале ключевое слово "while" (WHILE)
затем любое логическое выражение (expression)
далее минимум один переход на новую строку (NEWLINE+)
в конце блок кода (block)
 */
whileStatement: 
    WHILE expression NEWLINE+
    block;

// Правило оператора цикла 
/*
В начале ключевое слово "until" (UNTIL)
затем любое логическое выражение (expression)
далее минимум один переход на новую строку (NEWLINE+)
в конце блок кода (block)
 */
untilStatement: 
    UNTIL expression NEWLINE+
    block;
    
returnStatement: RETURN argumentList?; // Правило конструкции возврата значения из функции 
writeStatement: WRITE '(' argumentList? ')'; // Правило вызова фцнкции вывода 
readStatement: READ '(' argumentList? ')'; // Правило вызова функции ввода

// Правило описывающее все возможные выражения в языке
expression
    : primaryExpression                                             #primaryExpr // первичное (не рекурсивное) выражение
    | '|' expression '|'                                            #normExpr // выражение нормы/модуля
    | '-' expression                                                #unaryMinusExpr // выражение унарного минуса
    |'(' expression ')'                                             #parenExpr // выражение в скобках
    | expression '[' expression ']'                                 #indexExpr // выражение индексации
    | expression ('*' | '/') expression                             #mulDivExpr // выражение умножения/деления
    | expression ('+' | '-') expression                             #addSubExpr // выражения сложения/вычитания
    | expression ('>' | '<' | '>=' | '<=' | '==' | '!=') expression #comparisonExpr // выражения сравнения 
    | NOT expression                                                #notExpr // выражение логического отрицания
    | expression (AND | OR) expression                              #binlogicExpr // выражения логического И/ИЛИ
    ;

// правило типов (используется для вызова функций преобразования типов)
type
    : INT_TYPE // целое число
    | FLOAT_TYPE // число с плавающей точкой
    | VECTOR // вектор
    | MATRIX // матрица
    ;

// правило описывающее все первичные (не рекурсивные) выражения в языке
primaryExpression
    : ID '(' argumentList? ')'                          #funcCallExpr // вызов функции
    | var                                               #varExpr // переменная 
    | methodAppeal                                      #methodExpr // вызов метода класса
    | literal                                           #literalExpr // литерал
    | type '(' argumentList? ')'                        #typeExpr // вызов функции преобразования типов
    | LEN '(' argumentList? ')'                         #lenExpr // вызов функции взятия длины
    | readStatement                                     #readExpr // вызов функции ввода
    ;
    
argumentList: expression (',' expression)*; // правило описывающее список аргументов 

// правило построения литералов
literal
    :INT                                                             #intLiteral // литерал целого числа
    | FLOAT                                                          #floatLiteral // литерал числа с плавающей точкой
    | '[' argumentList ']'                                           #vectorLiteral // векторный литерал
    | '[' '[' argumentList ']' (',' '[' argumentList ']')* ']'       #matrixLiteral // матричный литерал
    | STRING                                                         #stringLiteral // литерал строки
    ;




