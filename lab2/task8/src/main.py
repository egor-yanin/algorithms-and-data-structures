from lab2.utils import read_array, write_vars


def addition(A, B, sign=True):
    if len(A) != len(B):
        if len(A) > len(B):
            n = len(A)
            B = (0,) * (n-len(B)) + B
        else:
            n = len(B)
            A = (0,) * (n - len(A)) + A
    if sign:
        return tuple(a + b for a, b in zip(A, B))
    else:
        return tuple(a - b for a, b in zip(A, B))


def multiply(A, B):
    if len(A) == len(B) == 1:
        return (A[0] * B[0], )
    n = len(A) // 2 * 2
    mid = len(A) // 2
    if len(A) % 2 == 0:
        a_1, a_2 = A[:mid], A[mid:]
        b_1, b_2 = B[:mid], B[mid:]
    else:
        a_1, a_2 = A[:mid+1], A[mid+1:]
        b_1, b_2 = B[:mid+1], B[mid+1:]
    c_1 = multiply(a_1, b_1)
    c_3 = multiply(a_2, b_2)
    add_1 = addition(a_1, a_2)
    add_2 = addition(b_1, b_2)
    c_2 = addition(addition(multiply(add_1, add_2), c_1, False), c_3, False)
    m_1 = c_1 + (0, ) * n
    m_2 = c_2 + (0, ) * (n // 2)
    m_3 = c_3
    return addition(addition(m_1, m_2), m_3)


def main(file='input.txt'):
    input_data = read_array(file, 1, 2)
    A, B = map(tuple, input_data)
    write_vars('../tests/output.txt', multiply(A, B))
