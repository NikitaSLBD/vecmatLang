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
        4,1,53,429,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,5,0,66,
        8,0,10,0,12,0,69,9,0,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,83,8,1,1,1,1,1,1,1,4,1,88,8,1,11,1,12,1,89,1,1,1,
        1,1,2,1,2,1,2,5,2,97,8,2,10,2,12,2,100,9,2,1,3,1,3,4,3,104,8,3,11,
        3,12,3,105,1,3,1,3,1,4,1,4,1,4,1,4,3,4,114,8,4,1,4,1,4,1,4,4,4,119,
        8,4,11,4,12,4,120,1,4,1,4,1,5,1,5,1,5,1,5,4,5,129,8,5,11,5,12,5,
        130,1,5,1,5,1,6,1,6,1,6,1,6,3,6,139,8,6,1,6,1,6,1,6,4,6,144,8,6,
        11,6,12,6,145,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,159,
        8,8,1,8,1,8,1,9,1,9,3,9,165,8,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,173,
        8,9,1,9,1,9,3,9,177,8,9,1,9,1,9,3,9,181,8,9,1,9,1,9,3,9,185,8,9,
        1,9,1,9,3,9,189,8,9,1,9,1,9,3,9,193,8,9,1,9,3,9,196,8,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,205,8,10,1,11,1,11,3,11,209,8,11,1,
        12,1,12,1,12,1,12,1,13,1,13,1,13,4,13,218,8,13,11,13,12,13,219,1,
        13,1,13,1,13,1,13,1,13,4,13,227,8,13,11,13,12,13,228,3,13,231,8,
        13,1,14,1,14,1,14,1,14,4,14,237,8,14,11,14,12,14,238,1,14,1,14,1,
        14,4,14,244,8,14,11,14,12,14,245,1,14,3,14,249,8,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,3,15,259,8,15,1,15,1,15,3,15,263,8,15,
        1,15,1,15,4,15,267,8,15,11,15,12,15,268,1,15,1,15,1,16,1,16,1,16,
        4,16,276,8,16,11,16,12,16,277,1,16,1,16,1,17,1,17,1,17,4,17,285,
        8,17,11,17,12,17,286,1,17,1,17,1,18,1,18,3,18,293,8,18,1,19,1,19,
        1,19,3,19,298,8,19,1,19,1,19,1,20,1,20,1,20,3,20,305,8,20,1,20,1,
        20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,319,8,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,5,21,338,8,21,10,21,12,21,341,9,21,1,22,1,
        22,1,23,1,23,1,23,3,23,348,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,3,23,362,8,23,1,23,1,23,1,23,1,23,1,
        23,3,23,369,8,23,1,23,1,23,3,23,373,8,23,1,24,1,24,1,24,5,24,378,
        8,24,10,24,12,24,381,9,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,389,
        8,25,10,25,12,25,392,9,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,
        401,8,25,10,25,12,25,404,9,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,
        412,8,25,10,25,12,25,415,9,25,1,25,1,25,5,25,419,8,25,10,25,12,25,
        422,9,25,1,25,1,25,1,25,3,25,427,8,25,1,25,0,1,42,26,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,5,
        1,0,11,12,2,0,10,10,13,13,1,0,14,19,1,0,42,43,1,0,45,48,481,0,55,
        1,0,0,0,2,78,1,0,0,0,4,93,1,0,0,0,6,101,1,0,0,0,8,109,1,0,0,0,10,
        124,1,0,0,0,12,134,1,0,0,0,14,149,1,0,0,0,16,153,1,0,0,0,18,195,
        1,0,0,0,20,204,1,0,0,0,22,208,1,0,0,0,24,210,1,0,0,0,26,214,1,0,
        0,0,28,232,1,0,0,0,30,250,1,0,0,0,32,272,1,0,0,0,34,281,1,0,0,0,
        36,290,1,0,0,0,38,294,1,0,0,0,40,301,1,0,0,0,42,318,1,0,0,0,44,342,
        1,0,0,0,46,372,1,0,0,0,48,374,1,0,0,0,50,426,1,0,0,0,52,54,5,21,
        0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,61,
        1,0,0,0,57,55,1,0,0,0,58,60,3,8,4,0,59,58,1,0,0,0,60,63,1,0,0,0,
        61,59,1,0,0,0,61,62,1,0,0,0,62,67,1,0,0,0,63,61,1,0,0,0,64,66,3,
        2,1,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,
        73,1,0,0,0,69,67,1,0,0,0,70,72,3,18,9,0,71,70,1,0,0,0,72,75,1,0,
        0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,
        5,0,0,1,77,1,1,0,0,0,78,79,5,32,0,0,79,80,5,49,0,0,80,82,5,1,0,0,
        81,83,3,4,2,0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,5,
        2,0,0,85,87,5,3,0,0,86,88,5,21,0,0,87,86,1,0,0,0,88,89,1,0,0,0,89,
        87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,3,6,3,0,92,3,1,0,0,
        0,93,98,5,49,0,0,94,95,5,4,0,0,95,97,5,49,0,0,96,94,1,0,0,0,97,100,
        1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,5,1,0,0,0,100,98,1,0,0,0,
        101,103,5,23,0,0,102,104,3,18,9,0,103,102,1,0,0,0,104,105,1,0,0,
        0,105,103,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,24,0,
        0,108,7,1,0,0,0,109,110,5,37,0,0,110,111,5,49,0,0,111,113,5,1,0,
        0,112,114,3,4,2,0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,
        0,115,116,5,2,0,0,116,118,5,3,0,0,117,119,5,21,0,0,118,117,1,0,0,
        0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,
        0,122,123,3,10,5,0,123,9,1,0,0,0,124,128,5,23,0,0,125,129,3,18,9,
        0,126,129,3,12,6,0,127,129,3,2,1,0,128,125,1,0,0,0,128,126,1,0,0,
        0,128,127,1,0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,
        0,131,132,1,0,0,0,132,133,5,24,0,0,133,11,1,0,0,0,134,135,5,38,0,
        0,135,136,5,49,0,0,136,138,5,1,0,0,137,139,3,4,2,0,138,137,1,0,0,
        0,138,139,1,0,0,0,139,140,1,0,0,0,140,141,5,2,0,0,141,143,5,3,0,
        0,142,144,5,21,0,0,143,142,1,0,0,0,144,145,1,0,0,0,145,143,1,0,0,
        0,145,146,1,0,0,0,146,147,1,0,0,0,147,148,3,6,3,0,148,13,1,0,0,0,
        149,150,5,49,0,0,150,151,5,5,0,0,151,152,5,49,0,0,152,15,1,0,0,0,
        153,154,5,49,0,0,154,155,5,5,0,0,155,156,5,49,0,0,156,158,5,1,0,
        0,157,159,3,48,24,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,1,0,
        0,0,160,161,5,2,0,0,161,17,1,0,0,0,162,164,3,22,11,0,163,165,5,21,
        0,0,164,163,1,0,0,0,164,165,1,0,0,0,165,196,1,0,0,0,166,196,3,28,
        14,0,167,196,3,30,15,0,168,196,3,32,16,0,169,196,3,34,17,0,170,172,
        3,42,21,0,171,173,5,21,0,0,172,171,1,0,0,0,172,173,1,0,0,0,173,196,
        1,0,0,0,174,176,3,36,18,0,175,177,5,21,0,0,176,175,1,0,0,0,176,177,
        1,0,0,0,177,196,1,0,0,0,178,180,3,38,19,0,179,181,5,21,0,0,180,179,
        1,0,0,0,180,181,1,0,0,0,181,196,1,0,0,0,182,184,3,40,20,0,183,185,
        5,21,0,0,184,183,1,0,0,0,184,185,1,0,0,0,185,196,1,0,0,0,186,188,
        5,39,0,0,187,189,5,21,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,196,
        1,0,0,0,190,192,5,40,0,0,191,193,5,21,0,0,192,191,1,0,0,0,192,193,
        1,0,0,0,193,196,1,0,0,0,194,196,5,21,0,0,195,162,1,0,0,0,195,166,
        1,0,0,0,195,167,1,0,0,0,195,168,1,0,0,0,195,169,1,0,0,0,195,170,
        1,0,0,0,195,174,1,0,0,0,195,178,1,0,0,0,195,182,1,0,0,0,195,186,
        1,0,0,0,195,190,1,0,0,0,195,194,1,0,0,0,196,19,1,0,0,0,197,205,5,
        49,0,0,198,205,3,14,7,0,199,200,5,49,0,0,200,201,5,6,0,0,201,202,
        3,42,21,0,202,203,5,7,0,0,203,205,1,0,0,0,204,197,1,0,0,0,204,198,
        1,0,0,0,204,199,1,0,0,0,205,21,1,0,0,0,206,209,3,24,12,0,207,209,
        3,26,13,0,208,206,1,0,0,0,208,207,1,0,0,0,209,23,1,0,0,0,210,211,
        3,20,10,0,211,212,5,8,0,0,212,213,3,42,21,0,213,25,1,0,0,0,214,217,
        3,20,10,0,215,216,5,4,0,0,216,218,3,20,10,0,217,215,1,0,0,0,218,
        219,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,
        230,5,8,0,0,222,231,3,46,23,0,223,226,3,42,21,0,224,225,5,4,0,0,
        225,227,3,42,21,0,226,224,1,0,0,0,227,228,1,0,0,0,228,226,1,0,0,
        0,228,229,1,0,0,0,229,231,1,0,0,0,230,222,1,0,0,0,230,223,1,0,0,
        0,231,27,1,0,0,0,232,233,5,25,0,0,233,234,3,42,21,0,234,236,5,26,
        0,0,235,237,5,21,0,0,236,235,1,0,0,0,237,238,1,0,0,0,238,236,1,0,
        0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,248,3,6,3,0,241,243,5,27,
        0,0,242,244,5,21,0,0,243,242,1,0,0,0,244,245,1,0,0,0,245,243,1,0,
        0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,249,3,6,3,0,248,241,1,0,
        0,0,248,249,1,0,0,0,249,29,1,0,0,0,250,251,5,28,0,0,251,252,5,49,
        0,0,252,253,5,29,0,0,253,254,5,36,0,0,254,255,5,1,0,0,255,258,3,
        42,21,0,256,257,5,4,0,0,257,259,3,42,21,0,258,256,1,0,0,0,258,259,
        1,0,0,0,259,262,1,0,0,0,260,261,5,4,0,0,261,263,3,42,21,0,262,260,
        1,0,0,0,262,263,1,0,0,0,263,264,1,0,0,0,264,266,5,2,0,0,265,267,
        5,21,0,0,266,265,1,0,0,0,267,268,1,0,0,0,268,266,1,0,0,0,268,269,
        1,0,0,0,269,270,1,0,0,0,270,271,3,6,3,0,271,31,1,0,0,0,272,273,5,
        30,0,0,273,275,3,42,21,0,274,276,5,21,0,0,275,274,1,0,0,0,276,277,
        1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,280,
        3,6,3,0,280,33,1,0,0,0,281,282,5,31,0,0,282,284,3,42,21,0,283,285,
        5,21,0,0,284,283,1,0,0,0,285,286,1,0,0,0,286,284,1,0,0,0,286,287,
        1,0,0,0,287,288,1,0,0,0,288,289,3,6,3,0,289,35,1,0,0,0,290,292,5,
        33,0,0,291,293,3,48,24,0,292,291,1,0,0,0,292,293,1,0,0,0,293,37,
        1,0,0,0,294,295,5,34,0,0,295,297,5,1,0,0,296,298,3,48,24,0,297,296,
        1,0,0,0,297,298,1,0,0,0,298,299,1,0,0,0,299,300,5,2,0,0,300,39,1,
        0,0,0,301,302,5,35,0,0,302,304,5,1,0,0,303,305,3,48,24,0,304,303,
        1,0,0,0,304,305,1,0,0,0,305,306,1,0,0,0,306,307,5,2,0,0,307,41,1,
        0,0,0,308,309,6,21,-1,0,309,319,3,46,23,0,310,311,5,9,0,0,311,312,
        3,42,21,0,312,313,5,9,0,0,313,319,1,0,0,0,314,315,5,10,0,0,315,319,
        3,42,21,7,316,317,5,44,0,0,317,319,3,42,21,2,318,308,1,0,0,0,318,
        310,1,0,0,0,318,314,1,0,0,0,318,316,1,0,0,0,319,339,1,0,0,0,320,
        321,10,5,0,0,321,322,7,0,0,0,322,338,3,42,21,6,323,324,10,4,0,0,
        324,325,7,1,0,0,325,338,3,42,21,5,326,327,10,3,0,0,327,328,7,2,0,
        0,328,338,3,42,21,4,329,330,10,1,0,0,330,331,7,3,0,0,331,338,3,42,
        21,2,332,333,10,6,0,0,333,334,5,6,0,0,334,335,3,42,21,0,335,336,
        5,7,0,0,336,338,1,0,0,0,337,320,1,0,0,0,337,323,1,0,0,0,337,326,
        1,0,0,0,337,329,1,0,0,0,337,332,1,0,0,0,338,341,1,0,0,0,339,337,
        1,0,0,0,339,340,1,0,0,0,340,43,1,0,0,0,341,339,1,0,0,0,342,343,7,
        4,0,0,343,45,1,0,0,0,344,345,5,49,0,0,345,347,5,1,0,0,346,348,3,
        48,24,0,347,346,1,0,0,0,347,348,1,0,0,0,348,349,1,0,0,0,349,373,
        5,2,0,0,350,373,3,20,10,0,351,352,5,1,0,0,352,353,3,42,21,0,353,
        354,5,2,0,0,354,373,1,0,0,0,355,373,3,14,7,0,356,373,3,16,8,0,357,
        373,3,50,25,0,358,359,3,44,22,0,359,361,5,1,0,0,360,362,3,48,24,
        0,361,360,1,0,0,0,361,362,1,0,0,0,362,363,1,0,0,0,363,364,5,2,0,
        0,364,373,1,0,0,0,365,366,5,41,0,0,366,368,5,1,0,0,367,369,3,48,
        24,0,368,367,1,0,0,0,368,369,1,0,0,0,369,370,1,0,0,0,370,373,5,2,
        0,0,371,373,3,40,20,0,372,344,1,0,0,0,372,350,1,0,0,0,372,351,1,
        0,0,0,372,355,1,0,0,0,372,356,1,0,0,0,372,357,1,0,0,0,372,358,1,
        0,0,0,372,365,1,0,0,0,372,371,1,0,0,0,373,47,1,0,0,0,374,379,3,42,
        21,0,375,376,5,4,0,0,376,378,3,42,21,0,377,375,1,0,0,0,378,381,1,
        0,0,0,379,377,1,0,0,0,379,380,1,0,0,0,380,49,1,0,0,0,381,379,1,0,
        0,0,382,427,5,50,0,0,383,427,5,51,0,0,384,385,5,6,0,0,385,390,3,
        42,21,0,386,387,5,4,0,0,387,389,3,42,21,0,388,386,1,0,0,0,389,392,
        1,0,0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,393,1,0,0,0,392,390,
        1,0,0,0,393,394,5,7,0,0,394,427,1,0,0,0,395,396,5,6,0,0,396,397,
        5,6,0,0,397,402,3,42,21,0,398,399,5,4,0,0,399,401,3,42,21,0,400,
        398,1,0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,0,403,
        405,1,0,0,0,404,402,1,0,0,0,405,420,5,7,0,0,406,407,5,4,0,0,407,
        408,5,6,0,0,408,413,3,42,21,0,409,410,5,4,0,0,410,412,3,42,21,0,
        411,409,1,0,0,0,412,415,1,0,0,0,413,411,1,0,0,0,413,414,1,0,0,0,
        414,416,1,0,0,0,415,413,1,0,0,0,416,417,5,7,0,0,417,419,1,0,0,0,
        418,406,1,0,0,0,419,422,1,0,0,0,420,418,1,0,0,0,420,421,1,0,0,0,
        421,423,1,0,0,0,422,420,1,0,0,0,423,424,5,7,0,0,424,427,1,0,0,0,
        425,427,5,52,0,0,426,382,1,0,0,0,426,383,1,0,0,0,426,384,1,0,0,0,
        426,395,1,0,0,0,426,425,1,0,0,0,427,51,1,0,0,0,52,55,61,67,73,82,
        89,98,105,113,120,128,130,138,145,158,164,172,176,180,184,188,192,
        195,204,208,219,228,230,238,245,248,258,262,268,277,286,292,297,
        304,318,337,339,347,361,368,372,379,390,402,413,420,426
    ]

class vecmatlangParser ( Parser ):

    grammarFileName = "vecmatlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "','", "'.'", "'['", 
                     "']'", "'='", "'|'", "'-'", "'*'", "'/'", "'+'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "<INVALID>", 
                     "<INVALID>", "'\\t'", "'<<INDENT>>'", "'<<DEDENT>>'", 
                     "'if'", "'then'", "'else'", "'for'", "'in'", "'while'", 
                     "'until'", "'func'", "'return'", "'write'", "'read'", 
                     "'range'", "'class'", "'method'", "'continue'", "'break'", 
                     "'len'", "'&&'", "'||'", "'!'", "'int'", "'float'", 
                     "'vector'", "'matrix'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "NEWLINE", "TAB", "INDENT", "DEDENT", "IF", 
                      "THEN", "ELSE", "FOR", "IN", "WHILE", "UNTIL", "FUNC", 
                      "RETURN", "WRITE", "READ", "RANGE", "CLASS", "METHOD", 
                      "CONTINUE", "BREAK", "LEN", "AND", "OR", "NOT", "INT_TYPE", 
                      "FLOAT_TYPE", "VECTOR", "MATRIX", "ID", "INT", "FLOAT", 
                      "STRING", "COMMENT" ]

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
    TAB=22
    INDENT=23
    DEDENT=24
    IF=25
    THEN=26
    ELSE=27
    FOR=28
    IN=29
    WHILE=30
    UNTIL=31
    FUNC=32
    RETURN=33
    WRITE=34
    READ=35
    RANGE=36
    CLASS=37
    METHOD=38
    CONTINUE=39
    BREAK=40
    LEN=41
    AND=42
    OR=43
    NOT=44
    INT_TYPE=45
    FLOAT_TYPE=46
    VECTOR=47
    MATRIX=48
    ID=49
    INT=50
    FLOAT=51
    STRING=52
    COMMENT=53

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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.ClassDeclContext,i)


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
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 52
                    self.match(vecmatlangParser.NEWLINE) 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 58
                self.classDecl()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 64
                self.functionDecl()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8993519014250050) != 0):
                self.state = 70
                self.statement()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
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

        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(vecmatlangParser.ParameterListContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

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
            self.state = 78
            self.match(vecmatlangParser.FUNC)
            self.state = 79
            self.match(vecmatlangParser.ID)
            self.state = 80
            self.match(vecmatlangParser.T__0)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 81
                self.parameterList()


            self.state = 84
            self.match(vecmatlangParser.T__1)
            self.state = 85
            self.match(vecmatlangParser.T__2)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.match(vecmatlangParser.NEWLINE)
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 91
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
            self.state = 93
            self.match(vecmatlangParser.ID)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 94
                self.match(vecmatlangParser.T__3)
                self.state = 95
                self.match(vecmatlangParser.ID)
                self.state = 100
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
            self.state = 101
            self.match(vecmatlangParser.INDENT)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.statement()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8993519014250050) != 0)):
                    break

            self.state = 107
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

        def classBody(self):
            return self.getTypedRuleContext(vecmatlangParser.ClassBodyContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(vecmatlangParser.ParameterListContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

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
            self.state = 109
            self.match(vecmatlangParser.CLASS)
            self.state = 110
            self.match(vecmatlangParser.ID)
            self.state = 111
            self.match(vecmatlangParser.T__0)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 112
                self.parameterList()


            self.state = 115
            self.match(vecmatlangParser.T__1)
            self.state = 116
            self.match(vecmatlangParser.T__2)
            self.state = 118 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self.match(vecmatlangParser.NEWLINE)
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 122
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


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.FunctionDeclContext,i)


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
            self.state = 124
            self.match(vecmatlangParser.INDENT)
            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 128
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 6, 9, 10, 21, 25, 28, 30, 31, 33, 34, 35, 39, 40, 41, 44, 45, 46, 47, 48, 49, 50, 51, 52]:
                    self.state = 125
                    self.statement()
                    pass
                elif token in [38]:
                    self.state = 126
                    self.methodDecl()
                    pass
                elif token in [32]:
                    self.state = 127
                    self.functionDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8993798187124290) != 0)):
                    break

            self.state = 132
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

        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(vecmatlangParser.ParameterListContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

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
            self.state = 134
            self.match(vecmatlangParser.METHOD)
            self.state = 135
            self.match(vecmatlangParser.ID)
            self.state = 136
            self.match(vecmatlangParser.T__0)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 137
                self.parameterList()


            self.state = 140
            self.match(vecmatlangParser.T__1)
            self.state = 141
            self.match(vecmatlangParser.T__2)
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.match(vecmatlangParser.NEWLINE)
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 147
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
            self.state = 149
            self.match(vecmatlangParser.ID)
            self.state = 150
            self.match(vecmatlangParser.T__4)
            self.state = 151
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
            self.state = 153
            self.match(vecmatlangParser.ID)
            self.state = 154
            self.match(vecmatlangParser.T__4)
            self.state = 155
            self.match(vecmatlangParser.ID)
            self.state = 156
            self.match(vecmatlangParser.T__0)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8991840451692098) != 0):
                self.state = 157
                self.argumentList()


            self.state = 160
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.assignment()
                self.state = 164
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 163
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.untilStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.expression(0)
                self.state = 172
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 171
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 174
                self.returnStatement()
                self.state = 176
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 175
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 178
                self.writeStatement()
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 182
                self.readStatement()
                self.state = 184
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 183
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 186
                self.match(vecmatlangParser.CONTINUE)
                self.state = 188
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 187
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 190
                self.match(vecmatlangParser.BREAK)
                self.state = 192
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 191
                    self.match(vecmatlangParser.NEWLINE)


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 194
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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(vecmatlangParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.fieldAppeal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(vecmatlangParser.ID)
                self.state = 200
                self.match(vecmatlangParser.T__5)
                self.state = 201
                self.expression(0)
                self.state = 202
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
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.singleAssignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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
            self.state = 210
            self.var()
            self.state = 211
            self.match(vecmatlangParser.T__7)
            self.state = 212
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
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.var()
            self.state = 217 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 215
                self.match(vecmatlangParser.T__3)
                self.state = 216
                self.var()
                self.state = 219 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 221
            self.match(vecmatlangParser.T__7)
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 222
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.state = 223
                self.expression(0)
                self.state = 226 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 224
                    self.match(vecmatlangParser.T__3)
                    self.state = 225
                    self.expression(0)
                    self.state = 228 
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

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(vecmatlangParser.BlockContext)
            else:
                return self.getTypedRuleContext(vecmatlangParser.BlockContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

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
            self.state = 232
            self.match(vecmatlangParser.IF)
            self.state = 233
            self.expression(0)
            self.state = 234
            self.match(vecmatlangParser.THEN)
            self.state = 236 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 235
                self.match(vecmatlangParser.NEWLINE)
                self.state = 238 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 240
            self.block()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 241
                self.match(vecmatlangParser.ELSE)
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 242
                    self.match(vecmatlangParser.NEWLINE)
                    self.state = 245 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==21):
                        break

                self.state = 247
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


        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(vecmatlangParser.FOR)
            self.state = 251
            self.match(vecmatlangParser.ID)
            self.state = 252
            self.match(vecmatlangParser.IN)
            self.state = 253
            self.match(vecmatlangParser.RANGE)
            self.state = 254
            self.match(vecmatlangParser.T__0)
            self.state = 255
            self.expression(0)
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 256
                self.match(vecmatlangParser.T__3)
                self.state = 257
                self.expression(0)


            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 260
                self.match(vecmatlangParser.T__3)
                self.state = 261
                self.expression(0)


            self.state = 264
            self.match(vecmatlangParser.T__1)
            self.state = 266 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 265
                self.match(vecmatlangParser.NEWLINE)
                self.state = 268 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 270
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


        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(vecmatlangParser.WHILE)
            self.state = 273
            self.expression(0)
            self.state = 275 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 274
                self.match(vecmatlangParser.NEWLINE)
                self.state = 277 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 279
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


        def block(self):
            return self.getTypedRuleContext(vecmatlangParser.BlockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(vecmatlangParser.NEWLINE)
            else:
                return self.getToken(vecmatlangParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(vecmatlangParser.UNTIL)
            self.state = 282
            self.expression(0)
            self.state = 284 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 283
                self.match(vecmatlangParser.NEWLINE)
                self.state = 286 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 288
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

        def argumentList(self):
            return self.getTypedRuleContext(vecmatlangParser.ArgumentListContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(vecmatlangParser.RETURN)
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 291
                self.argumentList()


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

        def argumentList(self):
            return self.getTypedRuleContext(vecmatlangParser.ArgumentListContext,0)


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
            self.state = 294
            self.match(vecmatlangParser.WRITE)
            self.state = 295
            self.match(vecmatlangParser.T__0)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8991840451692098) != 0):
                self.state = 296
                self.argumentList()


            self.state = 299
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

        def argumentList(self):
            return self.getTypedRuleContext(vecmatlangParser.ArgumentListContext,0)


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
            self.state = 301
            self.match(vecmatlangParser.READ)
            self.state = 302
            self.match(vecmatlangParser.T__0)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8991840451692098) != 0):
                self.state = 303
                self.argumentList()


            self.state = 306
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
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6, 35, 41, 45, 46, 47, 48, 49, 50, 51, 52]:
                localctx = vecmatlangParser.PrimaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 309
                self.primaryExpression()
                pass
            elif token in [9]:
                localctx = vecmatlangParser.NormExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 310
                self.match(vecmatlangParser.T__8)
                self.state = 311
                self.expression(0)
                self.state = 312
                self.match(vecmatlangParser.T__8)
                pass
            elif token in [10]:
                localctx = vecmatlangParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 314
                self.match(vecmatlangParser.T__9)
                self.state = 315
                self.expression(7)
                pass
            elif token in [44]:
                localctx = vecmatlangParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 316
                self.match(vecmatlangParser.NOT)
                self.state = 317
                self.expression(2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 337
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = vecmatlangParser.MulDivExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 320
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 321
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 322
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = vecmatlangParser.AddSubExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 323
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 324
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 325
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = vecmatlangParser.ComparisonExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 326
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 327
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 328
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = vecmatlangParser.BinlogicExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 329
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 330
                        _la = self._input.LA(1)
                        if not(_la==42 or _la==43):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 331
                        self.expression(2)
                        pass

                    elif la_ == 5:
                        localctx = vecmatlangParser.IndexExprContext(self, vecmatlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 332
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 333
                        self.match(vecmatlangParser.T__5)
                        self.state = 334
                        self.expression(0)
                        self.state = 335
                        self.match(vecmatlangParser.T__6)
                        pass

             
                self.state = 341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
            self.state = 342
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 527765581332480) != 0)):
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



    class VarExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(vecmatlangParser.VarContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


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


    class MethodExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def methodAppeal(self):
            return self.getTypedRuleContext(vecmatlangParser.MethodAppealContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodExpr" ):
                listener.enterMethodExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodExpr" ):
                listener.exitMethodExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodExpr" ):
                return visitor.visitMethodExpr(self)
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


    class ReadExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def readStatement(self):
            return self.getTypedRuleContext(vecmatlangParser.ReadStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadExpr" ):
                listener.enterReadExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadExpr" ):
                listener.exitReadExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadExpr" ):
                return visitor.visitReadExpr(self)
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


    class FieldExprContext(PrimaryExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a vecmatlangParser.PrimaryExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fieldAppeal(self):
            return self.getTypedRuleContext(vecmatlangParser.FieldAppealContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldExpr" ):
                listener.enterFieldExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldExpr" ):
                listener.exitFieldExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldExpr" ):
                return visitor.visitFieldExpr(self)
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



    def primaryExpression(self):

        localctx = vecmatlangParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_primaryExpression)
        self._la = 0 # Token type
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = vecmatlangParser.FuncCallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(vecmatlangParser.ID)
                self.state = 345
                self.match(vecmatlangParser.T__0)
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8991840451692098) != 0):
                    self.state = 346
                    self.argumentList()


                self.state = 349
                self.match(vecmatlangParser.T__1)
                pass

            elif la_ == 2:
                localctx = vecmatlangParser.VarExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.var()
                pass

            elif la_ == 3:
                localctx = vecmatlangParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 351
                self.match(vecmatlangParser.T__0)
                self.state = 352
                self.expression(0)
                self.state = 353
                self.match(vecmatlangParser.T__1)
                pass

            elif la_ == 4:
                localctx = vecmatlangParser.FieldExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.fieldAppeal()
                pass

            elif la_ == 5:
                localctx = vecmatlangParser.MethodExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 356
                self.methodAppeal()
                pass

            elif la_ == 6:
                localctx = vecmatlangParser.LiteralExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 357
                self.literal()
                pass

            elif la_ == 7:
                localctx = vecmatlangParser.TypeExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 358
                self.type_()
                self.state = 359
                self.match(vecmatlangParser.T__0)
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8991840451692098) != 0):
                    self.state = 360
                    self.argumentList()


                self.state = 363
                self.match(vecmatlangParser.T__1)
                pass

            elif la_ == 8:
                localctx = vecmatlangParser.LenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 365
                self.match(vecmatlangParser.LEN)
                self.state = 366
                self.match(vecmatlangParser.T__0)
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8991840451692098) != 0):
                    self.state = 367
                    self.argumentList()


                self.state = 370
                self.match(vecmatlangParser.T__1)
                pass

            elif la_ == 9:
                localctx = vecmatlangParser.ReadExprContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 371
                self.readStatement()
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
            self.state = 374
            self.expression(0)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 375
                self.match(vecmatlangParser.T__3)
                self.state = 376
                self.expression(0)
                self.state = 381
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
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                localctx = vecmatlangParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(vecmatlangParser.INT)
                pass

            elif la_ == 2:
                localctx = vecmatlangParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(vecmatlangParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = vecmatlangParser.VectorLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.match(vecmatlangParser.T__5)
                self.state = 385
                self.expression(0)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 386
                    self.match(vecmatlangParser.T__3)
                    self.state = 387
                    self.expression(0)
                    self.state = 392
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 393
                self.match(vecmatlangParser.T__6)
                pass

            elif la_ == 4:
                localctx = vecmatlangParser.MatrixLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.match(vecmatlangParser.T__5)
                self.state = 396
                self.match(vecmatlangParser.T__5)
                self.state = 397
                self.expression(0)
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 398
                    self.match(vecmatlangParser.T__3)
                    self.state = 399
                    self.expression(0)
                    self.state = 404
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 405
                self.match(vecmatlangParser.T__6)
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 406
                    self.match(vecmatlangParser.T__3)
                    self.state = 407
                    self.match(vecmatlangParser.T__5)
                    self.state = 408
                    self.expression(0)
                    self.state = 413
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==4:
                        self.state = 409
                        self.match(vecmatlangParser.T__3)
                        self.state = 410
                        self.expression(0)
                        self.state = 415
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 416
                    self.match(vecmatlangParser.T__6)
                    self.state = 422
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 423
                self.match(vecmatlangParser.T__6)
                pass

            elif la_ == 5:
                localctx = vecmatlangParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 425
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
         




