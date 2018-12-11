import numpy as np 
from scipy.signal import convolve2d as conv

grid_serial = 8868

highest = 0
best_x = 0
best_y = 0
best_size = 0

grid = np.zeros((300, 300))
for x in range(300):
    for y in range(300):
        rack_id = x + 10 + 1
        power_level = rack_id * (y + 1)
        power_level += grid_serial
        power_level *= rack_id
        digit = 0
        if power_level > 100:
            digit = int([a for a in str(power_level)][-3])
        digit -= 5
        grid[x, y] = digit

for size in range(1, 30):
    print(size)
    tmp = conv(grid, np.ones((size, size)))
    if np.max(tmp) < highest:
        continue
    for x in range(tmp.shape[0]):
        for y in range(tmp.shape[1]):
            if tmp[x,y] > highest:
                highest = tmp[x,y]
                best_x, best_y = x-size+2, y-size+2

                best_size = size
print(f"{best_x},{best_y},{best_size}")
