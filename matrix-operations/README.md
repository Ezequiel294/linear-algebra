# Matrix Operations

This repository contains Python scripts for performing matrix addition and multiplication using the numpy library and the Fraction module from the fractions library.

## Matrix Addition

This Python script performs matrix addition using numpy. The script prompts the user to input the dimensions and elements of two matrices, A and B, and then adds them together.

### Instructions

1. Run the script `matrix-addition.py` in your Python environment.
2. When prompted, enter the number of rows and columns for matrices A and B.
3. You will then be prompted to enter the elements of matrix A. Enter each element as a number and press enter.
4. Repeat the process for matrix B.
5. The script will then perform the matrix addition and print the result.

### Requirements

- Python 3.x
- numpy library

**Note:** The script uses numpy to handle matrix operations. This allows for efficient calculations with matrices.

## Matrix Multiplication

This Python script performs matrix multiplication using numpy and the Fraction module from the fractions library. The script prompts the user to input the dimensions and elements of two matrices, A and B, and then multiplies them together.

### Instructions

1. Run the script `matrix-multiplication.py` in your Python environment.
2. When prompted, enter the number of rows and columns for matrix A.
3. The number of rows for matrix B is automatically set to be equal to the number of columns of matrix A. This is necessary for matrix multiplication.
4. Enter the number of columns for matrix B.
5. You will then be prompted to enter the elements of matrix A. Enter each element as a fraction in the format 'numerator/denominator'. For example, to enter the fraction 3/4, type '3/4' (without the quotes) and press enter.
6. Repeat the process for matrix B.
7. The script will then perform the matrix multiplication and print the result.

### Requirements

- Python 3.x
- numpy library

**Note:** The script uses the Fraction class from the fractions library to handle fractional numbers. This allows for precise calculations with fractions, but it also means that you must enter all numbers as fractions. If you want to enter a whole number, enter it as 'number/1'. For example, to enter the number 2, type '2/1'.

