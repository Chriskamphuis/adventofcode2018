import numpy as np
patch = np.zeros((1000, 1000))

with open('input.txt') as f:
    for line in f:
        elements = line.split(' ')
        x, y = [int(e) for e in elements[2][:-1].split(',')]
        height, width = [int(e) for e in elements[3][:-1].split('x')]
        patch[x:x+height, y:y+width] += 1
print(np.sum(patch[patch>1].astype(np.bool).astype(np.int)))
