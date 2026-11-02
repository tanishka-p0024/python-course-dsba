import numpy as np
x = float(input('Enter the x-coordinate: '))
y = float(input('Enter the y-coordinate: '))
original_coordinate = (x,y)
theta = float(input('Enter the degree of rotation: '))
theta_rad = np.radians(theta)
x_1 = x*np.cos(theta_rad) - y*np.sin(theta_rad)
x_1 = round(x_1,2)
y_1 = y*np.cos(theta_rad) + x*np.sin(theta_rad)
y_1 = round(y_1,2)
new_coordinate = (x_1,y_1)

print(f'The rotation of point {original_coordinate} about {theta} deg is ({x_1:.2f}, {y_1:.2f})')
