# Linear Regression Program

This program is designed to perform simple linear regression on a set of data points provided by the user. Linear regression is a statistical method used to model the relationship between two variables by fitting a linear equation to observed data.

## Code Explanation

The fit_linear_line function takes a list of data points as input. Each data point is a tuple of two values (x, y). The function uses the numpy polyfit function to calculate the coefficients of the best fit line. These coefficients are returned as a tuple (m, b).

The main part of the script prompts the user to enter the number of data points and the x and y values for each point. These points are stored in a list and passed to the fit_linear_line function. The resulting line equation is then printed to the console.

**Note**
This program assumes that the relationship between the variables is linear. If the relationship is not linear, the results may not be accurate.

## How to Use

1. Run the linear_regression.py script.
   When prompted, enter the number of data points you want to use for the linear regression.
   For each data point, you will be asked to enter the x and y values. Enter these values as prompted.
   Once all data points have been entered, the program will calculate the coefficients of the best fit line using the least squares method.
   The equation of the line will be displayed in the format y = mx + b, where m is the slope of the line and b is the y-intercept.

## Requirements

- Python 3.x
- numpy library

