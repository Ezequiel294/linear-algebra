import numpy as np
from fractions import Fraction


n_rowsA = int(input("Enter the number of rows of matrix A: "))
n_colsA = int(input("Enter the number of columns of matrix A: "))
n_rowsB = n_colsA
print(f"The number of rows of matrix B has to be {n_rowsB}")
n_colsB = int(input("Enter the number of columns of matrix B: "))

A = np.zeros((n_rowsA, n_colsA))
B = np.zeros((n_rowsB, n_colsB))

print("\n")

for i in range(n_rowsA):
    for j in range(n_colsA):
        A[i][j] = Fraction(input(f"Enter the element matrix A[{i+1}][{j+1}] of matrix A: "))

print("\n")

for i in range(n_rowsB):
    for j in range(n_colsB):
        B[i][j] = Fraction(input(f"Enter the element in matrix B[{i+1}][{j+1}] of matrix B: "))

result = np.dot(A, B)
print(f"\n{result}")