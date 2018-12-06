import numpy as np

coordinates = []

with open('input.txt') as f:
    for line in f:
        x, y = line[:-1].split(', ')
        coordinates.append([int(x), int(y)])

amount = len(coordinates)
coordinates = np.array(coordinates)
max_x, max_y = coordinates.max(axis=0)
grid = np.zeros((max_x, max_y))

for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        distances = [abs(x - coordinate[0]) + abs(y - coordinate[1])
                     for coordinate in coordinates]
        if np.sum(distances) < 10000:
            grid[x, y] = 1

print(np.sum(grid))
