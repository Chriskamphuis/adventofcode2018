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
        lowest = np.argmin(distances)
        distances = sorted(distances)
        if distances[0] == distances[1]:
            grid[x, y] = -1
        else:
            grid[x, y] = lowest

infinites = set()
for x in range(max_x):
    infinites |= {grid[x, 0]}
    infinites |= {grid[x, max_y-1]}
for y in range(max_y):
    infinites |= {grid[0, y]}
    infinites |= {grid[max_x-1, y]}

max_area = 0
for i in range(amount):
    if i not in infinites:
        area = np.sum((grid == i).astype(np.bool).astype(np.int)) 
        if area > max_area:
            max_area = area

print(max_area)
