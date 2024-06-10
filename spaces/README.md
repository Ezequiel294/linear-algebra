# Spaces

This Python script, spaces.py, is designed to calculate the null space, column space, and row space of a given matrix. It uses the Singular Value Decomposition (SVD) method from the NumPy library to perform these calculations.

**find_null_space(matrix):** This function calculates the null space of the given matrix. The null space of a matrix is the set of all vectors that when multiplied by the matrix result in the zero vector.

**find_column_space(matrix):** This function calculates the column space of the given matrix. The column space of a matrix is the set of all possible linear combinations of its column vectors.

**find_row_space(matrix):** This function calculates the row space of the given matrix. The row space of a matrix is the set of all possible linear combinations of its row vectors.

**Note**
The script uses a tolerance of 1e-10 to determine the rank of the matrix in the SVD decomposition. This means that any singular values less than 1e-10 are considered to be zero. This tolerance can be adjusted as needed.

## Instructions

To use this script, you need to run it in a Python environment. When the script is run, it will prompt you to enter the number of rows and columns for the matrix. Then, it will ask you to input each element of the matrix one by one.

After you've entered all the elements, the script will calculate and print the null space, column space, and row space of the matrix.

## Requirements

1. Python 3.x
2. NumPy

