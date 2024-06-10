import numpy as np


def fit_linear_line(data_points):
    # Unpack the data points into two lists
    x_values, y_values = zip(*data_points)

    # The function returns the coefficients [m, b] of the fit line
    m, b = np.polyfit(x_values, y_values, 1)

    return m, b


points = int(input("Enter the amount of points: "))
data_points = list()

for i in range(points):
    x = float(input(f"Enter the x value of point {i+1}: "))
    y = float(input(f"Enter the y value of point {i+1}: "))
    data_points.append((x, y))

m, b = fit_linear_line(data_points)

m = round(m, 2)
b = round(b, 2)

print(f"\nLine: y = {m}x + {b}")

