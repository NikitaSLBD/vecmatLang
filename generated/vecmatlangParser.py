# Generated from d:/Programming/YAPIS/matveclang/vecmatLang/vecmatlang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,393,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,71,8,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,81,8,
        2,10,2,12,2,84,9,2,1,3,1,3,4,3,88,8,3,11,3,12,3,89,1,3,1,3,1,4,1,
        4,1,4,1,4,3,4,98,8,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,4,5,108,8,5,
        11,5,12,5,109,1,5,1,5,1,6,1,6,1,6,1,6,3,6,118,8,6,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,134,8,8,1,8,1,8,1,
        9,1,9,3,9,140,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,149,8,9,1,9,1,
        9,3,9,153,8,9,1,9,1,9,3,9,157,8,9,1,9,1,9,3,9,161,8,9,1,9,1,9,3,
        9,165,8,9,1,9,1,9,3,9,169,8,9,1,9,3,9,172,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,181,8,10,1,11,1,11,3,11,185,8,11,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,4,13,194,8,13,11,13,12,13,195,1,13,1,13,1,
        13,1,13,1,13,1,13,4,13,204,8,13,11,13,12,13,205,3,13,208,8,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,218,8,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,5,18,246,8,
        18,10,18,12,18,249,9,18,1,19,1,19,1,19,1,19,1,19,5,19,256,8,19,10,
        19,12,19,259,9,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,5,20,268,8,
        20,10,20,12,20,271,9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,3,21,285,8,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,304,
        8,21,10,21,12,21,307,9,21,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,3,23,319,8,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,327,8,
        23,1,23,1,23,1,23,1,23,1,23,3,23,334,8,23,1,23,3,23,337,8,23,1,24,
        1,24,1,24,5,24,342,8,24,10,24,12,24,345,9,24,1,25,1,25,1,25,1,25,
        1,25,1,25,5,25,353,8,25,10,25,12,25,356,9,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,5,25,365,8,25,10,25,12,25,368,9,25,1,25,1,25,1,25,
        1,25,1,25,1,25,5,25,376,8,25,10,25,12,25,379,9,25,1,25,1,25,5,25,
        383,8,25,10,25,12,25,386,9,25,1,25,1,25,1,25,3,25,391,8,25,1,25,
        0,1,42,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,0,5,1,0,11,12,2,0,10,10,13,13,1,0,14,19,1,0,41,
        42,1,0,44,47,431,0,55,1,0,0,0,2,66,1,0,0,0,4,77,1,0,0,0,6,85,1,0,
        0,0,8,93,1,0,0,0,10,104,1,0,0,0,12,113,1,0,0,0,14,124,1,0,0,0,16,
        128,1,0,0,0,18,171,1,0,0,0,20,180,1,0,0,0,22,184,1,0,0,0,24,186,
        1,0,0,0,26,207,1,0,0,0,28,209,1,0,0,0,30,219,1,0,0,0,32,231,1,0,
        0,0,34,236,1,0,0,0,36,241,1,0,0,0,38,250,1,0,0,0,40,262,1,0,0,0,
        42,284,1,0,0,0,44,308,1,0,0,0,46,336,1,0,0,0,48,338,1,0,0,0,50,390,
        1,0,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,
        55,56,1,0,0,0,56,61,1,0,0,0,57,55,1,0,0,0,58,60,3,18,9,0,59,58,1,
        0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,
        61,1,0,0,0,64,65,5,0,0,1,65,1,1,0,0,0,66,67,5,31,0,0,67,68,5,48,
        0,0,68,70,5,1,0,0,69,71,3,4,2,0,70,69,1,0,0,0,70,71,1,0,0,0,71,72,
        1,0,0,0,72,73,5,2,0,0,73,74,5,3,0,0,74,75,5,21,0,0,75,76,3,6,3,0,
        76,3,1,0,0,0,77,82,5,48,0,0,78,79,5,4,0,0,79,81,5,48,0,0,80,78,1,
        0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,5,1,0,0,0,84,
        82,1,0,0,0,85,87,5,22,0,0,86,88,3,18,9,0,87,86,1,0,0,0,88,89,1,0,
        0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,23,0,0,92,
        7,1,0,0,0,93,94,5,36,0,0,94,95,5,48,0,0,95,97,5,1,0,0,96,98,3,4,
        2,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,5,2,0,0,100,
        101,5,3,0,0,101,102,5,21,0,0,102,103,3,10,5,0,103,9,1,0,0,0,104,
        107,5,22,0,0,105,108,3,18,9,0,106,108,3,12,6,0,107,105,1,0,0,0,107,
        106,1,0,0,0,108,109,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,
        111,1,0,0,0,111,112,5,23,0,0,112,11,1,0,0,0,113,114,5,37,0,0,114,
        115,5,48,0,0,115,117,5,1,0,0,116,118,3,4,2,0,117,116,1,0,0,0,117,
        118,1,0,0,0,118,119,1,0,0,0,119,120,5,2,0,0,120,121,5,3,0,0,121,
        122,5,21,0,0,122,123,3,6,3,0,123,13,1,0,0,0,124,125,5,48,0,0,125,
        126,5,5,0,0,126,127,5,48,0,0,127,15,1,0,0,0,128,129,5,48,0,0,129,
        130,5,5,0,0,130,131,5,48,0,0,131,133,5,1,0,0,132,134,3,48,24,0,133,
        132,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,5,2,0,0,136,
        17,1,0,0,0,137,139,3,22,11,0,138,140,5,21,0,0,139,138,1,0,0,0,139,
        140,1,0,0,0,140,172,1,0,0,0,141,172,3,8,4,0,142,172,3,28,14,0,143,
        172,3,30,15,0,144,172,3,32,16,0,145,172,3,34,17,0,146,148,3,42,21,
        0,147,149,5,21,0,0,148,147,1,0,0,0,148,149,1,0,0,0,149,172,1,0,0,
        0,150,152,3,36,18,0,151,153,5,21,0,0,152,151,1,0,0,0,152,153,1,0,
        0,0,153,172,1,0,0,0,154,156,3,38,19,0,155,157,5,21,0,0,156,155,1,
        0,0,0,156,157,1,0,0,0,157,172,1,0,0,0,158,160,3,40,20,0,159,161,
        5,21,0,0,160,159,1,0,0,0,160,161,1,0,0,0,161,172,1,0,0,0,162,164,
        5,38,0,0,163,165,5,21,0,0,164,163,1,0,0,0,164,165,1,0,0,0,165,172,
        1,0,0,0,166,168,5,39,0,0,167,169,5,21,0,0,168,167,1,0,0,0,168,169,
        1,0,0,0,169,172,1,0,0,0,170,172,5,21,0,0,171,137,1,0,0,0,171,141,
        1,0,0,0,171,142,1,0,0,0,171,143,1,0,0,0,171,144,1,0,0,0,171,145,
        1,0,0,0,171,146,1,0,0,0,171,150,1,0,0,0,171,154,1,0,0,0,171,158,
        1,0,0,0,171,162,1,0,0,0,171,166,1,0,0,0,171,170,1,0,0,0,172,19,1,
        0,0,0,173,181,5,48,0,0,174,181,3,14,7,0,175,176,5,48,0,0,176,177,
        5,6,0,0,177,178,3,42,21,0,178,179,5,7,0,0,179,181,1,0,0,0,180,173,
        1,0,0,0,180,174,1,0,0,0,180,175,1,0,0,0,181,21,1,0,0,0,182,185,3,
        24,12,0,183,185,3,26,13,0,184,182,1,0,0,0,184,183,1,0,0,0,185,23,
        1,0,0,0,186,187,3,20,10,0,187,188,5,8,0,0,188,189,3,42,21,0,189,
        25,1,0,0,0,190,193,3,20,10,0,191,192,5,4,0,0,192,194,3,20,10,0,193,
        191,1,0,0,0,194,195,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,
        197,1,0,0,0,197,198,5,8,0,0,198,199,3,46,23,0,199,208,1,0,0,0,200,
        203,3,42,21,0,201,202,5,4,0,0,202,204,3,42,21,0,203,201,1,0,0,0,
        204,205,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,
        207,190,1,0,0,0,207,200,1,0,0,0,208,27,1,0,0,0,209,210,5,24,0,0,
        210,211,3,42,21,0,211,212,5,25,0,0,212,213,5,21,0,0,213,217,3,6,
        3,0,214,215,5,26,0,0,215,216,5,21,0,0,216,218,3,6,3,0,217,214,1,
        0,0,0,217,218,1,0,0,0,218,29,1,0,0,0,219,220,5,27,0,0,220,221,5,
        48,0,0,221,222,5,28,0,0,222,223,5,35,0,0,223,224,5,1,0,0,224,225,
        3,42,21,0,225,226,5,4,0,0,226,227,3,42,21,0,227,228,5,2,0,0,228,
        229,5,21,0,0,229,230,3,6,3,0,230,31,1,0,0,0,231,232,5,29,0,0,232,
        233,3,42,21,0,233,234,5,21,0,0,234,235,3,6,3,0,235,33,1,0,0,0,236,
        237,5,30,0,0,237,238,3,42,21,0,238,239,5,21,0,0,239,240,3,6,3,0,
        240,35,1,0,0,0,241,242,5,32,0,0,242,247,3,42,21,0,243,244,5,4,0,
        0,244,246,3,42,21,0,245,243,1,0,0,0,246,249,1,0,0,0,247,245,1,0,
        0,0,247,248,1,0,0,0,248,37,1,0,0,0,249,247,1,0,0,0,250,251,5,33,
        0,0,251,252,5,1,0,0,252,257,3,42,21,0,253,254,5,4,0,0,254,256,3,
        42,21,0,255,253,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,258,
        1,0,0,0,258,260,1,0,0,0,259,257,1,0,0,0,260,261,5,2,0,0,261,39,1,
        0,0,0,262,263,5,34,0,0,263,264,5,1,0,0,264,269,3,42,21,0,265,266,
        5,4,0,0,266,268,3,42,21,0,267,265,1,0,0,0,268,271,1,0,0,0,269,267,
        1,0,0,0,269,270,1,0,0,0,270,272,1,0,0,0,271,269,1,0,0,0,272,273,
        5,2,0,0,273,41,1,0,0,0,274,275,6,21,-1,0,275,285,3,46,23,0,276,277,
        5,9,0,0,277,278,3,42,21,0,278,279,5,9,0,0,279,285,1,0,0,0,280,281,
        5,10,0,0,281,285,3,42,21,7,282,283,5,43,0,0,283,285,3,42,21,2,284,
        274,1,0,0,0,284,276,1,0,0,0,284,280,1,0,0,0,284,282,1,0,0,0,285,
        305,1,0,0,0,286,287,10,5,0,0,287,288,7,0,0,0,288,304,3,42,21,6,289,
        290,10,4,0,0,290,291,7,1,0,0,291,304,3,42,21,5,292,293,10,3,0,0,
        293,294,7,2,0,0,294,304,3,42,21,4,295,296,10,1,0,0,296,297,7,3,0,
        0,297,304,3,42,21,2,298,299,10,6,0,0,299,300,5,6,0,0,300,301,3,42,
        21,0,301,302,5,7,0,0,302,304,1,0,0,0,303,286,1,0,0,0,303,289,1,0,
        0,0,303,292,1,0,0,0,303,295,1,0,0,0,303,298,1,0,0,0,304,307,1,0,
        0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,43,1,0,0,0,307,305,1,0,0,
        0,308,309,7,4,0,0,309,45,1,0,0,0,310,337,5,48,0,0,311,312,5,1,0,
        0,312,313,3,42,21,0,313,314,5,2,0,0,314,337,1,0,0,0,315,316,5,48,
        0,0,316,318,5,1,0,0,317,319,3,48,24,0,318,317,1,0,0,0,318,319,1,
        0,0,0,319,320,1,0,0,0,320,337,5,2,0,0,321,337,3,50,25,0,322,337,
        3,20,10,0,323,324,3,44,22,0,324,326,5,1,0,0,325,327,3,48,24,0,326,
        325,1,0,0,0,326,327,1,0,0,0,327,328,1,0,0,0,328,329,5,2,0,0,329,
        337,1,0,0,0,330,331,5,40,0,0,331,333,5,1,0,0,332,334,3,48,24,0,333,
        332,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,337,5,2,0,0,336,
        310,1,0,0,0,336,311,1,0,0,0,336,315,1,0,0,0,336,321,1,0,0,0,336,
        322,1,0,0,0,336,323,1,0,0,0,336,330,1,0,0,0,337,47,1,0,0,0,338,343,
        3,42,21,0,339,340,5,4,0,0,340,342,3,42,21,0,341,339,1,0,0,0,342,
        345,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,49,1,0,0,0,345,343,
        1,0,0,0,346,391,5,49,0,0,347,391,5,50,0,0,348,349,5,6,0,0,349,354,
        3,42,21,0,350,351,5,4,0,0,351,353,3,42,21,0,352,350,1,0,0,0,353,
        356,1,0,0,0,354,352,1,0,0,0,354,355,1,0,0,0,355,357,1,0,0,0,356,
        354,1,0,0,0,357,358,5,7,0,0,358,391,1,0,0,0,359,360,5,6,0,0,360,
        361,5,6,0,0,361,366,3,42,21,0,362,363,5,4,0,0,363,365,3,42,21,0,
        364,362,1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,
        367,369,1,0,0,0,368,366,1,0,0,0,369,384,5,7,0,0,370,371,5,4,0,0,
        371,372,5,6,0,0,372,377,3,42,21,0,373,374,5,4,0,0,374,376,3,42,21,
        0,375,373,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,
        0,378,380,1,0,0,0,379,377,1,0,0,0,380,381,5,7,0,0,381,383,1,0,0,
        0,382,370,1,0,0,0,383,386,1,0,0,0,384,382,1,0,0,0,384,385,1,0,0,
        0,385,387,1,0,0,0,386,384,1,0,0,0,387,388,5,7,0,0,388,391,1,0,0,
        0,389,391,5,51,0,0,390,346,1,0,0,0,390,347,1,0,0,0,390,348,1,0,0,
        0,390,359,1,0,0,0,390,389,1,0,0,0,391,51,1,0,0,0,40,55,61,70,82,
        89,97,107,109,117,133,139,148,152,156,160,164,168,171,180,184,195,
        205,207,217,247,257,269,284,303,305,318,326,333,336,343,354,366,
        377,384,390
    ]

class vecmatlangParser ( Parser ):

    grammarFileName = "vecmatlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "','", "'.'", "'['", 
                     "']'", "'='", "'|'", "'-'", "'*'", "'/'", "'+'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "<INVALID>", 
                     "<INVALID>", "'INDENT'", "'DEDENT'", "'if'", "'then'", 
                     "'else'", "'for'", "'in'", "'while'", "'until'", "'func'", 
                     "'return'", "'write'", "'read'", "'range'", "'class'", 
                     "'method'", "'continue'", "'exit'", "'len'", "'&&'", 
                     "'||'", "'!'", "'int'", "'float'", "'vector'", "'matrix'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "NEWLINE", "INDENT", "DEDENT", "IF", "THEN", 
                      "ELSE", "FOR", "IN", "WHILE", "UNTIL", "FUNC", "RETURN", 
                      "WRITE", "READ", "RANGE", "CLASS", "METHOD", "CONTINUE", 
                      "BREAK", "LEN", "AND", "OR", "NOT", "INT_TYPE", "FLOAT_TYPE", 
                      "VECTOR", "MATRIX", "ID", "INT", "FLOAT", "STRING", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_parameterList = 2
    RULE_block = 3
    RULE_classDecl = 4
    RULE_classBody = 5
    RULE_methodDecl = 6
    RULE_fieldAppeal = 7
    RULE_methodAppeal = 8
    RULE_statement = 9
    RULE_var = 10
    RULE_assignment = 11
    RULE_singleAssignment = 12
    RULE_multipleAssignment = 13
    RULE_ifStatement = 14
    RULE_forStatement = 15
    RULE_whileStatement = 16
    RULE_untilStatement = 17
    RULE_returnStatement = 18
    RULE_writeStatement = 19
    RULE_readStatement = 20
    RULE_expression = 21
    RULE_type = 22
    RULE_primaryExpression = 23
    RULE_argumentList = 24
    RULE_literal = 25

    ruleNames =  [ "program", "functionDecl", "parameterList", "block", 
                   "classDecl", "classBody", "methodDecl", "fieldAppeal", 
                   "methodAppeal", "statement", "var", "assignment", "singleAssignment", 
                   "multipleAssignment", "ifStatement", "forStatement", 
                   "whileStatement", "untilStatement", "returnStatement", 
                   "writeStatement", "readStatement", "expression", "type", 
                   "primaryExpression", "argumentList", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    WS=20
    NEWLINE=21
    INDENT=22
    DEDENT=23
    IF=24
    THEN=25
    ELSE=26
    FOR=27
    IN=28
    WHILE=29
    UNTIL=30
    FUNC=31
    RETURN=32
    WRITE=33
    READ=34
    RANGE=35
    CLASS=36
    METHOD=37
    CONTINUE=38
    BREAK=39
    LEN=40
    AND=41
    OR=42
    NOT=43
    INT_TYPE=44
    FLOAT_TYPE=45
    VECTOR=46
    MATRIX=47
    ID=48
    INT=49
    FLOAT=50
    STRING=51
    COMMENT=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(vecmatlangParser.EOF, 0)

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.FunctionDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.StatementContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.StatementContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = vecmatlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 52
                self.functionDecl()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4496828227651138) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(vecmatlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(vecmatlangParser.FUNC, 0)

        def ID(self):
            return self.getToken(vecmatlangParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(vecmatlangParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(vecmatlangParser.ParameterListContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = vecmatlangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(vecmatlangParser.FUNC)
            self.state = 67
            self.match(vecmatlangParser.ID)
            self.state = 68
            self.match(vecmatlangParser.T__0)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 69
                self.parameterList()


            self.state = 72
            self.match(vecmatlangParser.T__1)
            self.state = 73
            self.match(vecmatlangParser.T__2)
            self.state = 74
            self.match(vecmatlangParser.NEWLINE)
            self.state = 75
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.ID)
            else:
                return self.getToken(vecmatlangParser.ID, i)

        def getRuleIndex(self):
            return vecmatlangParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = vecmatlangParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(vecmatlangParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 78
                self.match(vecmatlangParser.T__3)
                self.state = 79
                self.match(vecmatlangParser.ID)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(vecmatlangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(vecmatlangParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.StatementContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.StatementContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = vecmatlangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(vecmatlangParser.INDENT)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.statement()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4496828227651138) != 0)):
                    break

            self.state = 91
            self.match(vecmatlangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(vecmatlangParser.CLASS, 0)

        def ID(self):
            return self.getToken(vecmatlangParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(vecmatlangParser.NEWLINE, 0)

        def classBody(self):
            return self.getTypedRuleContext(vecmatlangParser.ClassBodyContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(vecmatlangParser.ParameterListContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = vecmatlangParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(vecmatlangParser.CLASS)
            self.state = 94
            self.match(vecmatlangParser.ID)
            self.state = 95
            self.match(vecmatlangParser.T__0)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 96
                self.parameterList()


            self.state = 99
            self.match(vecmatlangParser.T__1)
            self.state = 100
            self.match(vecmatlangParser.T__2)
            self.state = 101
            self.match(vecmatlangParser.NEWLINE)
            self.state = 102
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(vecmatlangParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(vecmatlangParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.StatementContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.StatementContext,i)


        def methodDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.MethodDeclContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.MethodDeclContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = vecmatlangParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(vecmatlangParser.INDENT)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 6, 9, 10, 21, 24, 27, 29, 30, 32, 33, 34, 36, 38, 39, 40, 43, 44, 45, 46, 47, 48, 49, 50, 51]:
                    self.state = 105
                    self.statement()
                    pass
                elif token in [37]:
                    self.state = 106
                    self.methodDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4496965666604610) != 0)):
                    break

            self.state = 111
            self.match(vecmatlangParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METHOD(self):
            return self.getToken(vecmatlangParser.METHOD, 0)

        def ID(self):
            return self.getToken(vecmatlangParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(vecmatlangParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(vecmatlangParser.ParameterListContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = vecmatlangParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(vecmatlangParser.METHOD)
            self.state = 114
            self.match(vecmatlangParser.ID)
            self.state = 115
            self.match(vecmatlangParser.T__0)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 116
                self.parameterList()


            self.state = 119
            self.match(vecmatlangParser.T__1)
            self.state = 120
            self.match(vecmatlangParser.T__2)
            self.state = 121
            self.match(vecmatlangParser.NEWLINE)
            self.state = 122
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAppealContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.ID)
            else:
                return self.getToken(vecmatlangParser.ID, i)

        def getRuleIndex(self):
            return vecmatlangParser.RULE_fieldAppeal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAppeal" ):
                listener.enterFieldAppeal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAppeal" ):
                listener.exitFieldAppeal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAppeal" ):
                return visitor.visitFieldAppeal(self)
            else:
                return visitor.visitChildren(self)




    def fieldAppeal(self):

        localctx = vecmatlangParser.FieldAppealContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fieldAppeal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(vecmatlangParser.ID)
            self.state = 125
            self.match(vecmatlangParser.T__4)
            self.state = 126
            self.match(vecmatlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodAppealContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.ID)
            else:
                return self.getToken(vecmatlangParser.ID, i)

        def argumentList(self):
            return self.getTypedRuleContext(vecmatlangParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_methodAppeal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodAppeal" ):
                listener.enterMethodAppeal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodAppeal" ):
                listener.exitMethodAppeal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodAppeal" ):
                return visitor.visitMethodAppeal(self)
            else:
                return visitor.visitChildren(self)




    def methodAppeal(self):

        localctx = vecmatlangParser.MethodAppealContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_methodAppeal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(vecmatlangParser.ID)
            self.state = 129
            self.match(vecmatlangParser.T__4)
            self.state = 130
            self.match(vecmatlangParser.ID)
            self.state = 131
            self.match(vecmatlangParser.T__0)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4495903045977666) != 0):
                self.state = 132
                self.argumentList()


            self.state = 135
            self.match(vecmatlangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(vecmatlangParser.AssignmentContext,0)


        def NEWLINE(self):
            return self.getToken(vecmatlangParser.NEWLINE, 0)

        def classDecl(self):
            return self.getTypedRuleContext(vecmatlangParser.ClassDeclContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.WhileStatementContext,0)


        def untilStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.UntilStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.ReturnStatementContext,0)


        def writeStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.WriteStatementContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.ReadStatementContext,0)


        def CONTINUE(self):
            return self.getToken(vecmatlangParser.CONTINUE, 0)

        def BREAK(self):
            return self.getToken(vecmatlangParser.BREAK, 0)

        def getRuleIndex(self):
            return vecmatlangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = vecmatlangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.assignment()
                self.state = 139
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 138
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.classDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 145
                self.untilStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 146
                self.expression(0)
                self.state = 148
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 147
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 150
                self.returnStatement()
                self.state = 152
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 151
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 154
                self.writeStatement()
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 155
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 158
                self.readStatement()
                self.state = 160
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 159
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 162
                self.match(vecmatlangParser.CONTINUE)
                self.state = 164
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 163
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 166
                self.match(vecmatlangParser.BREAK)
                self.state = 168
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 167
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 170
                self.match(vecmatlangParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(vecmatlangParser.ID, 0)

        def fieldAppeal(self):
            return self.getTypedRuleContext(vecmatlangParser.FieldAppealContext,0)


        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = vecmatlangParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(vecmatlangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.fieldAppeal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.match(vecmatlangParser.ID)
                self.state = 176
                self.match(vecmatlangParser.T__5)
                self.state = 177
                self.expression(0)
                self.state = 178
                self.match(vecmatlangParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleAssignment(self):
            return self.getTypedRuleContext(vecmatlangParser.SingleAssignmentContext,0)


        def multipleAssignment(self):
            return self.getTypedRuleContext(vecmatlangParser.MultipleAssignmentContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = vecmatlangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.singleAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.multipleAssignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(vecmatlangParser.VarContext,0)


        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_singleAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleAssignment" ):
                listener.enterSingleAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleAssignment" ):
                listener.exitSingleAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleAssignment" ):
                return visitor.visitSingleAssignment(self)
            else:
                return visitor.visitChildren(self)




    def singleAssignment(self):

        localctx = vecmatlangParser.SingleAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_singleAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.var()
            self.state = 187
            self.match(vecmatlangParser.T__7)
            self.state = 188
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultipleAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.VarContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.VarContext,i)


        def primaryExpression(self):
            return self.getTypedRuleContext(vecmatlangParser.PrimaryExpressionContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_multipleAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultipleAssignment" ):
                listener.enterMultipleAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultipleAssignment" ):
                listener.exitMultipleAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultipleAssignment" ):
                return visitor.visitMultipleAssignment(self)
            else:
                return visitor.visitChildren(self)




    def multipleAssignment(self):

        localctx = vecmatlangParser.MultipleAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_multipleAssignment)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.var()
                self.state = 193 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 191
                    self.match(vecmatlangParser.T__3)
                    self.state = 192
                    self.var()
                    self.state = 195 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 197
                self.match(vecmatlangParser.T__7)
                self.state = 198
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.expression(0)
                self.state = 203 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 201
                    self.match(vecmatlangParser.T__3)
                    self.state = 202
                    self.expression(0)
                    self.state = 205 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(vecmatlangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(vecmatlangParser.THEN, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.BlockContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(vecmatlangParser.ELSE, 0)

        def getRuleIndex(self):
            return vecmatlangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = vecmatlangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(vecmatlangParser.IF)
            self.state = 210
            self.expression(0)
            self.state = 211
            self.match(vecmatlangParser.THEN)
            self.state = 212
            self.match(vecmatlangParser.NEWLINE)
            self.state = 213
            self.block()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 214
                self.match(vecmatlangParser.ELSE)
                self.state = 215
                self.match(vecmatlangParser.NEWLINE)
                self.state = 216
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(vecmatlangParser.FOR, 0)

        def ID(self):
            return self.getToken(vecmatlangParser.ID, 0)

        def IN(self):
            return self.getToken(vecmatlangParser.IN, 0)

        def RANGE(self):
            return self.getToken(vecmatlangParser.RANGE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def NEWLINE(self):
            return self.getToken(vecmatlangParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = vecmatlangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(vecmatlangParser.FOR)
            self.state = 220
            self.match(vecmatlangParser.ID)
            self.state = 221
            self.match(vecmatlangParser.IN)
            self.state = 222
            self.match(vecmatlangParser.RANGE)
            self.state = 223
            self.match(vecmatlangParser.T__0)
            self.state = 224
            self.expression(0)
            self.state = 225
            self.match(vecmatlangParser.T__3)
            self.state = 226
            self.expression(0)
            self.state = 227
            self.match(vecmatlangParser.T__1)
            self.state = 228
            self.match(vecmatlangParser.NEWLINE)
            self.state = 229
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(vecmatlangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(vecmatlangParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = vecmatlangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(vecmatlangParser.WHILE)
            self.state = 232
            self.expression(0)
            self.state = 233
            self.match(vecmatlangParser.NEWLINE)
            self.state = 234
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UntilStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNTIL(self):
            return self.getToken(vecmatlangParser.UNTIL, 0)

        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(vecmatlangParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_untilStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntilStatement" ):
                listener.enterUntilStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntilStatement" ):
                listener.exitUntilStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUntilStatement" ):
                return visitor.visitUntilStatement(self)
            else:
                return visitor.visitChildren(self)




    def untilStatement(self):

        localctx = vecmatlangParser.UntilStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_untilStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(vecmatlangParser.UNTIL)
            self.state = 237
            self.expression(0)
            self.state = 238
            self.match(vecmatlangParser.NEWLINE)
            self.state = 239
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(vecmatlangParser.RETURN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = vecmatlangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(vecmatlangParser.RETURN)
            self.state = 242
            self.expression(0)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 243
                self.match(vecmatlangParser.T__3)
                self.state = 244
                self.expression(0)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(vecmatlangParser.WRITE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_writeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)




    def writeStatement(self):

        localctx = vecmatlangParser.WriteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_writeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(vecmatlangParser.WRITE)
            self.state = 251
            self.match(vecmatlangParser.T__0)
            self.state = 252
            self.expression(0)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 253
                self.match(vecmatlangParser.T__3)
                self.state = 254
                self.expression(0)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self.match(vecmatlangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(vecmatlangParser.READ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_readStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)




    def readStatement(self):

        localctx = vecmatlangParser.ReadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(vecmatlangParser.READ)
            self.state = 263
            self.match(vecmatlangParser.T__0)
            self.state = 264
            self.expression(0)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 265
                self.match(vecmatlangParser.T__3)
                self.state = 266
                self.expression(0)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self.match(vecmatlangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return vecmatlangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IndexExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexExpr" ):
                listener.enterIndexExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexExpr" ):
                listener.exitIndexExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexExpr" ):
                return visitor.visitIndexExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(vecmatlangParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primaryExpression(self):
            return self.getTypedRuleContext(vecmatlangParser.PrimaryExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinlogicExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(vecmatlangParser.AND, 0)
        def OR(self):
            return self.getToken(vecmatlangParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinlogicExpr" ):
                listener.enterBinlogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinlogicExpr" ):
                listener.exitBinlogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinlogicExpr" ):
                return visitor.visitBinlogicExpr(self)
            else:
                return visitor.visitChildren(self)


    class NormExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormExpr" ):
                listener.enterNormExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormExpr" ):
                listener.exitNormExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormExpr" ):
                return visitor.visitNormExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = vecmatlangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6, 40, 44, 45, 46, 47, 48, 49, 50, 51]:
                localctx = vecmatlangParser.PrimaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 275
                self.primaryExpression()
                pass
            elif token in [9]:
                localctx = vecmatlangParser.NormExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 276
                self.match(vecmatlangParser.T__8)
                self.state = 277
                self.expression(0)
                self.state = 278
                self.match(vecmatlangParser.T__8)
                pass
            elif token in [10]:
                localctx = vecmatlangParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 280
                self.match(vecmatlangParser.T__9)
                self.state = 281
                self.expression(7)
                pass
            elif token in [43]:
                localctx = vecmatlangParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 282
                self.match(vecmatlangParser.NOT)
                self.state = 283
                self.expression(2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 303
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = vecmatlangParser.MulDivExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 286
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 287
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 288
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = vecmatlangParser.AddSubExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 289
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 290
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 291
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = vecmatlangParser.ComparisonExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 292
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 293
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 294
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = vecmatlangParser.BinlogicExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 295
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 296
                        _la = self._input.LA(1)
                        if not(_la==41 or _la==42):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 297
                        self.expression(2)
                        pass

                    elif la_ == 5:
                        localctx = vecmatlangParser.IndexExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 298
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 299
                        self.match(vecmatlangParser.T__5)
                        self.state = 300
                        self.expression(0)
                        self.state = 301
                        self.match(vecmatlangParser.T__6)
                        pass

             
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(vecmatlangParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(vecmatlangParser.FLOAT_TYPE, 0)

        def VECTOR(self):
            return self.getToken(vecmatlangParser.VECTOR, 0)

        def MATRIX(self):
            return self.getToken(vecmatlangParser.MATRIX, 0)

        def getRuleIndex(self):
            return vecmatlangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = vecmatlangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 263882790666240) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return vecmatlangParser.RULE_primaryExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LenExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEN(self):
            return self.getToken(vecmatlangParser.LEN, 0)
        def argumentList(self):
            return self.getTypedRuleContext(vecmatlangParser.ArgumentListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLenExpr" ):
                listener.enterLenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLenExpr" ):
                listener.exitLenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLenExpr" ):
                return visitor.visitLenExpr(self)
            else:
                return visitor.visitChildren(self)


    class TypeExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(vecmatlangParser.TypeContext,0)

        def argumentList(self):
            return self.getTypedRuleContext(vecmatlangParser.ArgumentListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeExpr" ):
                listener.enterTypeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeExpr" ):
                listener.exitTypeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpr" ):
                return visitor.visitTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(vecmatlangParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(vecmatlangParser.ID, 0)
        def argumentList(self):
            return self.getTypedRuleContext(vecmatlangParser.ArgumentListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(vecmatlangParser.ID, 0)
        def var(self):
            return self.getTypedRuleContext(vecmatlangParser.VarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def primaryExpression(self):

        localctx = vecmatlangParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_primaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                localctx = vecmatlangParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(vecmatlangParser.ID)
                pass

            elif la_ == 2:
                localctx = vecmatlangParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.match(vecmatlangParser.T__0)
                self.state = 312
                self.expression(0)
                self.state = 313
                self.match(vecmatlangParser.T__1)
                pass

            elif la_ == 3:
                localctx = vecmatlangParser.FuncCallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.match(vecmatlangParser.ID)
                self.state = 316
                self.match(vecmatlangParser.T__0)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4495903045977666) != 0):
                    self.state = 317
                    self.argumentList()


                self.state = 320
                self.match(vecmatlangParser.T__1)
                pass

            elif la_ == 4:
                localctx = vecmatlangParser.LiteralExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 321
                self.literal()
                pass

            elif la_ == 5:
                localctx = vecmatlangParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 322
                self.var()
                pass

            elif la_ == 6:
                localctx = vecmatlangParser.TypeExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 323
                self.type_()
                self.state = 324
                self.match(vecmatlangParser.T__0)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4495903045977666) != 0):
                    self.state = 325
                    self.argumentList()


                self.state = 328
                self.match(vecmatlangParser.T__1)
                pass

            elif la_ == 7:
                localctx = vecmatlangParser.LenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 330
                self.match(vecmatlangParser.LEN)
                self.state = 331
                self.match(vecmatlangParser.T__0)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4495903045977666) != 0):
                    self.state = 332
                    self.argumentList()


                self.state = 335
                self.match(vecmatlangParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return vecmatlangParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = vecmatlangParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.expression(0)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 339
                self.match(vecmatlangParser.T__3)
                self.state = 340
                self.expression(0)
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return vecmatlangParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VectorLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVectorLiteral" ):
                listener.enterVectorLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVectorLiteral" ):
                listener.exitVectorLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorLiteral" ):
                return visitor.visitVectorLiteral(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(vecmatlangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(vecmatlangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class MatrixLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixLiteral" ):
                listener.enterMatrixLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixLiteral" ):
                listener.exitMatrixLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixLiteral" ):
                return visitor.visitMatrixLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(vecmatlangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = vecmatlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = vecmatlangParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(vecmatlangParser.INT)
                pass

            elif la_ == 2:
                localctx = vecmatlangParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(vecmatlangParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = vecmatlangParser.VectorLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 348
                self.match(vecmatlangParser.T__5)
                self.state = 349
                self.expression(0)
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 350
                    self.match(vecmatlangParser.T__3)
                    self.state = 351
                    self.expression(0)
                    self.state = 356
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 357
                self.match(vecmatlangParser.T__6)
                pass

            elif la_ == 4:
                localctx = vecmatlangParser.MatrixLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 359
                self.match(vecmatlangParser.T__5)
                self.state = 360
                self.match(vecmatlangParser.T__5)
                self.state = 361
                self.expression(0)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 362
                    self.match(vecmatlangParser.T__3)
                    self.state = 363
                    self.expression(0)
                    self.state = 368
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 369
                self.match(vecmatlangParser.T__6)
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 370
                    self.match(vecmatlangParser.T__3)
                    self.state = 371
                    self.match(vecmatlangParser.T__5)
                    self.state = 372
                    self.expression(0)
                    self.state = 377
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==4:
                        self.state = 373
                        self.match(vecmatlangParser.T__3)
                        self.state = 374
                        self.expression(0)
                        self.state = 379
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 380
                    self.match(vecmatlangParser.T__6)
                    self.state = 386
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 387
                self.match(vecmatlangParser.T__6)
                pass

            elif la_ == 5:
                localctx = vecmatlangParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 389
                self.match(vecmatlangParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




