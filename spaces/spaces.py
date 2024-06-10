import numpy as np


def find_null_space(matrix):
    _, s, vh = np.linalg.svd(matrix)
    rank = np.sum(s > 1e-10)
    null_space = vh[rank:].T
    return null_space


def find_column_space(matrix):
    _, s, vh = np.linalg.svd(matrix)
    rank = np.sum(s > 1e-10)
    column_space = vh[:rank].T
    return column_space


def find_row_space(matrix):
    _, s, vh = np.linalg.svd(matrix)
    rank = np.sum(s > 1e-10)
    row_space = vh[:rank]
    return row_space


numberRows = int(input("Enter the number of rows: "))
numberColumns = int(input("Enter the number of columns: "))

matrix = []
for i in range(numberRows):
    row = []
    for j in range(numberColumns):
        row.append(float(input(f"Enter element A[{i+1}][{j+1}]: ")))
    matrix.append(row)
    print("\n")

npMatrix = np.array(matrix)
print(
    f"Null space: \n{find_null_space(npMatrix)}\n Column space: \n{find_column_space(npMatrix)}\n Row space: \n{find_row_space(npMatrix)}"
)

