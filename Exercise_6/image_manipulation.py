import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('/Users/classyytanugmail.com/Desktop/Python_DSBA/Python Exercises/python-course-dsba/Exercise_6/canva-MAHA8XxHPJk.jpeg')
# print(img.shape)
blue = img[:, :, 2]
# plt.imshow(blue,cmap='gray')
# plt.show()

# gray = np.mean(img, axis=2)
# plt.imsave('grayscale.jpg', gray, cmap='gray')

gray_weighted = (
    0.30 * img[:, :, 0] +
    0.59 * img[:, :, 1] +
    0.11 * img[:, :, 2]
)
plt.imsave('weighted_grayscale.jpg', gray_weighted, cmap='gray')