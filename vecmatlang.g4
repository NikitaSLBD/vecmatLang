grammar vecmatlang;

// Parser
program: functionDecl* statement* EOF;

functionDecl: FUNC ID '(' parameterList? ')' ':' NEWLINE block;
parameterList: ID (',' ID)*;

block: INDENT statement+ DEDENT;

classDecl: CLASS ID '(' parameterList? ')' ':' NEWLINE classBody;
classBody: INDENT (statement | methodDecl)+ DEDENT;

methodDecl: METHOD ID '(' parameterList? ')' ':' NEWLINE block;

fieldAppeal: ID '.' ID;
methodAppeal: ID '.' ID '(' argumentList? ')';

statement
    : assignment NEWLINE? 
    | classDecl
    | ifStatement   
    | forStatement
    | whileStatement
    | untilStatement
    | expression NEWLINE?
    | returnStatement NEWLINE?
    | writeStatement NEWLINE?
    | readStatement NEWLINE?
    | CONTINUE NEWLINE?
    | BREAK NEWLINE?
    | NEWLINE
    ;

var 
    : ID
    | fieldAppeal
    | ID '[' expression ']'
    ;

assignment: singleAssignment | multipleAssignment;
singleAssignment: var '=' expression;
multipleAssignment: var (',' var)+ '=' primaryExpression | expression (',' expression)+;

ifStatement: 
    IF expression THEN NEWLINE 
    block
    (ELSE NEWLINE block)?;

forStatement: 
    FOR ID IN RANGE '(' expression ',' expression ')' NEWLINE
    block;

whileStatement: 
    WHILE expression NEWLINE 
    block;

untilStatement: 
    UNTIL expression NEWLINE
    block;
    
returnStatement: RETURN expression (',' expression)*;

writeStatement: WRITE '(' expression (',' expression)* ')';
readStatement: READ '(' expression (',' expression)* ')';

expression
    : primaryExpression                                     #primaryExpr
    | '|' expression '|'                                    #normExpr
    | '-' expression                                        #unaryMinusExpr
    | expression '[' expression ']'                         #indexExpr
    | expression ('*' | '/') expression                     #mulDivExpr
    | expression ('+' | '-') expression                     #addSubExpr
    | expression ('>' | '<' | '>=' | '<=' | '==' | '!=') expression #comparisonExpr
    | NOT expression                                        #notExpr
    | expression (AND | OR) expression                      #binlogicExpr;

type
    : INT_TYPE
    | FLOAT_TYPE
    | VECTOR
    | MATRIX
    ;

primaryExpression
    : ID                                                #idExpr
    |'(' expression ')'                                 #parenExpr
    | ID '(' argumentList? ')'                          #funcCallExpr
    | literal                                           #literalExpr
    | var                                               #idExpr
    | type '(' argumentList? ')'                        #typeExpr
    | LEN '(' argumentList? ')'                         #lenExpr
    ;
    
argumentList: expression (',' expression)*;

literal
    :INT                                                #intLiteral
    | FLOAT                                             #floatLiteral
    | '[' expression (',' expression)* ']'              #vectorLiteral
    | '[' '[' expression (',' expression)* ']' (',' '[' expression (',' expression)* ']')* ']' #matrixLiteral
    | STRING                                            #stringLiteral
    ;

// Lexer
WS: [ ]+ -> skip;
NEWLINE: '\r'? '\n';
INDENT: 'INDENT' { /* Вставка через код */ };
DEDENT: 'DEDENT' { /* Вставка через код */ };


// Keywords
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
BREAK: 'exit';
LEN: 'len';

// Logical operators
AND: '&';
OR: '|';
NOT: '!';

// Types
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
VECTOR: 'vector';
MATRIX: 'matrix';

// Literals
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+;
STRING: '"' (~["\\\r\n] | '\\' ["\\])* '"';

COMMENT: '#' ~[\r\n]* -> skip;
