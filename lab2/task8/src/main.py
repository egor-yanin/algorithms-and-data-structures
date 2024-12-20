from lab2.utils import read_array, write_vars
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')


def addition(polynom_a, polynom_b, sign_is_plus=True):
    if len(polynom_a) != len(polynom_b):
        if len(polynom_a) > len(polynom_b):
            n = len(polynom_a)
            polynom_b = (0,) * (n - len(polynom_b)) + polynom_b
        else:
            n = len(polynom_b)
            polynom_a = (0,) * (n - len(polynom_a)) + polynom_a
    if sign_is_plus:
        return tuple(a + b for a, b in zip(polynom_a, polynom_b))
    else:
        return tuple(a - b for a, b in zip(polynom_a, polynom_b))


def multiply(polynom_a, polynom_b):
    if len(polynom_a) == len(polynom_b) == 1:
        return (polynom_a[0] * polynom_b[0],)
    n = len(polynom_a) - (len(polynom_a) % 2)
    mid = len(polynom_a) // 2
    if len(polynom_a) % 2 == 0:
        a_1, a_2 = polynom_a[:mid], polynom_a[mid:]
        b_1, b_2 = polynom_b[:mid], polynom_b[mid:]
    else:
        a_1, a_2 = polynom_a[:mid + 1], polynom_a[mid + 1:]
        b_1, b_2 = polynom_b[:mid + 1], polynom_b[mid + 1:]
    c_1 = multiply(a_1, b_1)
    c_3 = multiply(a_2, b_2)
    add_1 = addition(a_1, a_2)
    add_2 = addition(b_1, b_2)
    c_2 = addition(addition(multiply(add_1, add_2), c_1, False), c_3, False)
    m_1 = c_1 + (0, ) * n
    m_2 = c_2 + (0, ) * (n // 2)
    m_3 = c_3
    return addition(addition(m_1, m_2), m_3)


def task8():
    input_data = read_array(FILE_INPUT, 1, 2, with_len=False)
    A, B = map(tuple, input_data)
    write_vars(FILE_OUTPUT, multiply(A, B))


if __name__ == '__main__':
    task8()
