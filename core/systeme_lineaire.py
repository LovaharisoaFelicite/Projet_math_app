import numpy as np

def solve_with_numpy(A, b):
    """Résout AX=b avec numpy.linalg.solve"""
    return np.linalg.solve(A, b)

def solve_with_gauss(A, b):
    """Résout AX=b avec la méthode de Gauss manuelle"""
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    # Élimination
    for i in range(n):
        max_row = np.argmax(abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    # Substitution arrière
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x
