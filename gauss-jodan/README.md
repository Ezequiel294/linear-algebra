# Gauss-Jordan Elimination Method

This Python script implements the Gauss-Jordan method for solving systems of linear equations.

## Usage

1. Run the script. It will first ask you to enter the number of rows and columns for your matrix. This matrix represents the coefficients of the variables in your system of linear equations.

2. The script will then display an empty matrix of the size you specified.

3. Next, you will be asked to fill in the values for each cell in the matrix. Enter the coefficients of the variables in your equations, row by row.

4. After the matrix is filled, the script will start the Gauss-Jordan elimination process. For each step, you will be asked to enter the row and column of the pivot element. The pivot element is the one you want to make 1 and use to eliminate other elements in the same column.

5. If you enter a pivot row or column that is less than or equal to 0, the script will stop asking for pivot elements and end the Gauss-Jordan elimination process.

6. After each step, the script will print the current state of the matrix.

## Notes

- The row and column numbers start from 1, not 0.
- The matrix should be augmented, i.e., it should include the constants on the right side of the equations.

