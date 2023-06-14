import matplotlib.pyplot as plt
import numpy as np
from time import sleep


def draw_circle_square(matrix, circle_center, square_corner, radius, value):
    # Dimensions of the matrix
    height, width = matrix.shape

    # Coordinates of the circle center
    x_center, y_center = circle_center

    # Coordinates of the top-left corner of the square
    x_square, y_square = square_corner

    # Creating matrix indices
    x_indices = np.arange(width)
    y_indices = np.arange(height)

    # Creating coordinate grids
    x, y = np.meshgrid(x_indices, y_indices)

    # Calculating the distance between each point in the matrix and the circle center
    distance = np.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)

    # Updating values inside the circle
    matrix[distance <= radius] = value
    matrix[(x >= x_square) & (x <= x_square + radius) &
           (y >= y_square) & (y <= y_square + radius)] = value / 2

    # Adding the square
    distance = np.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)

    return matrix


if __name__ == '__main__':
    plt.figure(figsize=(8, 8))

    radius = 250
    circle, square = 0, 0
    vals = []

    # Creating a 1000x1000 matrix filled with zeros
    matrix = np.zeros((1000, 1000))

    # Drawing a circle with radius 2 and value 1
    matrix = draw_circle_square(matrix, (700, 700), (150, 150), radius, 1)
    sleep(2)

    for i in range(10000):
        ss_matrix = matrix.copy()
        random_point = np.random.randint(0, 1000), np.random.randint(0, 1000)

        plt.clf()
        plt.subplot(3, 1, 1)
        plt.imshow(ss_matrix, cmap='gray')
        plt.scatter(random_point[0], random_point[1], c='r')

        if ss_matrix[random_point[0], random_point[1]] == 1:
            circle += 1
        elif ss_matrix[random_point[0], random_point[1]] == 0.5:
            square += 1

        if i % 10 == 0 and i > 20:
            vals.append(circle / square)

        plt.subplot(3, 1, 2)
        plt.plot(vals)
        plt.hlines(np.pi, 0, len(vals), color='r')
        plt.subplot(3, 1, 3)
        plt.bar(['circle', 'square'], [circle, square], color=['r', 'b'])

        plt.pause(0.01)
