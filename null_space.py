import numpy as np

def null_space(A, tol=1e-13):
    u, s, vh = np.linalg.svd(A)
    null_mask = (s <= tol)
    null_space = vh[null_mask, :]
    return null_space.T

numberOfRows = int(input("Enter number of rows of your matrix: "))
numberOfColumns = int(input("Enter number of columns of your matrix: "))

A = np.zeros((numberOfRows, numberOfColumns))

for i in range(numberOfRows):
    for j in range(numberOfColumns):
        A[i][j] = float(input(f"Enter element of matrix[{i+1}][{j+1}]: "))

null_space = null_space(A)
print(f"Null space of matrix A is: \n{null_space}")