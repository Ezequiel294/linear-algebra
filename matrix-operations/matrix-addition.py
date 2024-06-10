import numpy as np

n_rows = int(input("Enter the number of rows of your matrices: "))
n_cols = int(input("Enter the number of columns of your matrices: "))

A = np.zeros((n_rows, n_cols))
B = A.copy()

print("\n")

for i in range(n_rows):
    for j in range(n_cols):
        A[i][j] = input(
            f"Enter the element in matrix A[{i+1}][{j+1}] of the first matrix: "
        )

print("\n")

for i in range(n_rows):
    for j in range(n_cols):
        B[i][j] = input(
            f"Enter the element in matrix B[{i+1}][{j+1}] of the second matrix: "
        )

result = np.add(A, B)
print(f"\n{result}")

