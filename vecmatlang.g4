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
* встроенные функции: read(), write(), len(), range()
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
после оператора присваивания может быть либо вызов функции (primaryExpression), либо перечисление выражений, минимум 2 
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
    

returnStatement: RETURN argumentList?;
writeStatement: WRITE '(' argumentList? ')';
readStatement: READ '(' argumentList? ')';

expression
    : primaryExpression                                             #primaryExpr
    | '|' expression '|'                                            #normExpr
    | '-' expression                                                #unaryMinusExpr
    | expression '[' expression ']'                                 #indexExpr
    | expression ('*' | '/') expression                             #mulDivExpr
    | expression ('+' | '-') expression                             #addSubExpr
    | expression ('>' | '<' | '>=' | '<=' | '==' | '!=') expression #comparisonExpr
    | NOT expression                                                #notExpr
    | expression (AND | OR) expression                              #binlogicExpr
    ;

type
    : INT_TYPE
    | FLOAT_TYPE
    | VECTOR
    | MATRIX
    ;

primaryExpression
    : ID '(' argumentList? ')'                          #funcCallExpr
    | var                                               #varExpr
    |'(' expression ')'                                 #parenExpr
    | fieldAppeal                                       #fieldExpr
    | methodAppeal                                      #methodExpr
    | literal                                           #literalExpr
    | type '(' argumentList? ')'                        #typeExpr
    | LEN '(' argumentList? ')'                         #lenExpr
    | readStatement                                     #readExpr
    ;
    
argumentList: expression (',' expression)*;


literal
    :INT                                                #intLiteral
    | FLOAT                                             #floatLiteral
    | '[' expression (',' expression)* ']'              #vectorLiteral
    | '[' '[' expression (',' expression)* ']' (',' '[' expression (',' expression)* ']')* ']' #matrixLiteral
    | STRING                                            #stringLiteral
    ;
