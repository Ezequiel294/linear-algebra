import numpy as np


def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return L, U


A = np.array([[3, 3, -4], [9, 12, -10]], dtype='float')
L, U = lu(A)
print(L)
print(U)
