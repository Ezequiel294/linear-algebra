import numpy as np


def get_pivot_coordinates():
    pivot_row = int(input("Enter Pivot Element row: "))
    pivot_column = int(input("Enter Pivot Element column: "))
    return pivot_row, pivot_column


def normalize_pivot_row(matrix, pivot_row, pivot_column):
    pivot_element = matrix[pivot_row][pivot_column]
    matrix[pivot_row] /= pivot_element


def update_other_rows(matrix, rows, pivot_row, pivot_column):
    for i in range(rows):
        if i != pivot_row:
            pivot_value = matrix[i][pivot_column]
            matrix[i] -= pivot_value * matrix[pivot_row]


rows = int(input("Enter Number of rows: "))
cols = int(input("Enter Number of columns: "))

matrix = np.zeros((rows, cols))

print(f"\n{matrix}\n")

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = float(input(f"Enter Number in Matrix[{i+1}][{j+1}]: "))

print(f"\n{matrix}")

for i in range(rows):
    print("\n")
    pivot_row, pivot_column = get_pivot_coordinates()

    if pivot_row <= 0 or pivot_column <= 0:
        break

    pivot_row -= 1
    pivot_column -= 1

    normalize_pivot_row(matrix, pivot_row, pivot_column)
    update_other_rows(matrix, rows, pivot_row, pivot_column)

    print(f"\n{matrix}")