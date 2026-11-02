'''Write a program that computes the new position of a point rotated by an angle 𝜃
 about the origin. 
 𝑥′ = 𝑥 cos 𝜃 − 𝑦 sin 𝜃, 𝑦′ = 𝑥 sin 𝜃 + 𝑦 cos 𝜃
Rotate a point by 𝜋/2 four times. 
Do you get exactly the starting point back? Explain what you see.'''

import numpy as np
x = float(input('Enter the x-coordinate: '))
y = float(input('Enter the y-coordinate: '))
original_coordinate = (x,y)
theta = float(input('Enter the degree of rotation: '))
theta_rad = np.radians(theta)



for r in range(2):
    x_new = x*np.cos(theta_rad) - y*np.sin(theta_rad)
    y_new = y*np.cos(theta_rad) + x*np.sin(theta_rad)
    x,y = x_new,y_new
x_new = round(x,2)
y_new = round(y,2)

new_coordinates = (x_new,y_new)
print(f'The rotation of point {original_coordinate} about {theta} deg is ({x_new:.2f}, {y_new:.2f})')