from enum import Enum
from typing import Dict, List, Optional, Tuple

class Type(Enum):
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    VECTOR = "vector"
    MATRIX = "matrix"
    VOID = "void"
    CLASS = "class"
    STRING = "string"
    UNKNOWN = "unknown"
    
    @staticmethod
    def from_token(token_type: int):
        mapping = {
            45: Type.INT,      # INT_TYPE
            46: Type.FLOAT,    # FLOAT_TYPE
            47: Type.VECTOR,   # VECTOR
            48: Type.MATRIX,   # MATRIX
            52: Type.STRING,   # STRING
        }
        return mapping.get(token_type, Type.UNKNOWN)

class Symbol:
    def __init__(self, name: str, symbol_type: Type, line: int = 0, column: int = 0, class_ref: str=None):
        self.name: str = name
        self.type: Type = symbol_type
        self.line: int = line
        self.column: int= column
        self.is_initialized: bool = False
        self.class_ref: str = class_ref
        
    def __str__(self):
        return f"{self.name}: {self.type.value}"

class FunctionSymbol(Symbol):
    def __init__(self, name: str, return_type: Type, params: List[Type], 
                 line: int = 0, column: int = 0, is_method: bool = False):
        super().__init__(name, return_type, line, column)
        self.params: List[Type] = params  # List of types
        self.is_method: bool = is_method
        self.overloads: List[List[Type]]= [params]  # Первая сигнатура сразу добавляется в overloads
        
    def add_overload(self, params: List[Type]):
        """Добавить перегрузку функции"""

        # Проверяем, нет ли уже такой перегрузки
        for overload in self.overloads:
            if len(overload) == len(params):
                # Уже есть перегрузка с таким количеством параметров
                return
        self.overloads.append(params)
        
    def find_matching_overload(self, arg_count: int) -> Optional[List[Type]]:
        """Найти подходящую перегрузку по количеству аргументов"""

        for overload in self.overloads:
            if len(overload) == arg_count:
                return overload
        return None
        
    def get_all_overloads_info(self) -> str:
        """Получить информацию о всех перегрузках"""

        overloads_info = []
        for _, overload in enumerate(self.overloads):
            overloads_info.append(f"{self.name}({len(overload)} аргументов)")
        return ", ".join(overloads_info)

class ClassSymbol(Symbol):
    def __init__(self, name: str, line: int = 0, column: int = 0):
        super().__init__(name, Type.CLASS, line, column)
        self.fields: Dict[str, Symbol] = {}
        self.methods: Dict[str, FunctionSymbol] = {}
        self.static_funcs: Dict[str, FunctionSymbol] = {}
        self.constructor_params: List[str] = []
        
    def add_constructor_param(self, name: str):
        self.constructor_params.append(name)

    def add_field(self, name: str, field_type: Type, line: int, column: int):
        self.fields[name] = Symbol(name, field_type, line, column)
        
    def add_method(self, name: str, return_type: Type, params: List[Type], 
                   line: int, column: int):
        self.methods[name] = FunctionSymbol(name, return_type, params, line, column, True)
        
    def add_static_func(self, name: str, return_type: Type, params: List[Type], 
                        line: int, column: int):
        self.static_funcs[name] = FunctionSymbol(name, return_type, params, line, column, False)
