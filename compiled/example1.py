import numpy as np

# -*- coding: utf-8 -*-

# ========== Встроенные функции ==========
def _vml_write(*args):
    for arg in args:
        # Убираем все лишние преобразования
        print(str(arg), end='')
    print()  # Добавляем перевод строки

def _vml_read(prompt=''):
    import sys
    if sys.platform == 'win32':
        import io
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    if prompt:
        sys.stdout.write(str(prompt))
        sys.stdout.flush()
    return sys.stdin.readline().strip()

def _vml_norm(x):
    if isinstance(x, (int, float)):
        return abs(x)
    elif isinstance(x, np.ndarray):
        return np.linalg.norm(x)
    elif isinstance(x, list):
        return np.linalg.norm(np.array(x, dtype=np.float64))
    return 0

def _vml_len(x):
    if isinstance(x, list):
        return len(x)
    elif isinstance(x, np.ndarray):
        if len(x.shape) == 1:
            return x.shape[0]
        else:
            return x.shape[0]
    return 0

def _vml_vector_mult(a, b):
    # Умножение векторов (скалярное) или вектора на число
    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        if len(a.shape) == 1 and len(b.shape) == 1:
            return np.dot(a, b)
    elif isinstance(a, np.ndarray) and isinstance(b, (int, float)):
        return a * b
    elif isinstance(a, (int, float)) and isinstance(b, np.ndarray):
        return b * a
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b  # Простое умножение чисел
    return a * b

def _vml_matrix_mult(a, b):
    # Умножение матриц или матрицы на число/вектор
    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        if len(a.shape) == 2 and len(b.shape) == 2:
            return np.dot(a, b)
        elif len(a.shape) == 2 and len(b.shape) == 1:
            return np.dot(a, b)
    elif isinstance(a, np.ndarray) and isinstance(b, (int, float)):
        return a * b
    elif isinstance(a, (int, float)) and isinstance(b, np.ndarray):
        return b * a
    return a * b

write = _vml_write
read = _vml_read

def _main_():
    i1 = 3
    f1 = 2.86
    n1 = i1 - f1
    v1 = np.array([1, 2, 3], dtype=np.float64)
    v2 = np.array([4, 5, 6], dtype=np.float64)
    sum_v = (v1 + _vml_vector_mult(v2, n1))
    len_sum_v = _vml_norm(sum_v)
    m1 = np.array([np.array([1, 2], dtype=np.float64), np.array([3, 4], dtype=np.float64)], dtype=np.float64)
    m2 = np.array([np.array([0, 1], dtype=np.float64), np.array([1, 0], dtype=np.float64)], dtype=np.float64)
    prod_m = (_vml_matrix_mult(m1, m2) * m1[1])
    if len_sum_v > 10:
        i2 = 5
        write("Vectors sum length more than 10")
    i2 = 7
    write("Vectors sum length less than 10")
else:
    write(i2)