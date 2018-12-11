import numpy as np
import matplotlib.pyplot as plt

messages = []

with open('input.txt') as f:
    for line in f:
        x, y = int(line[10:16]), int(line[18:24])
        dx, dy = int(line[-8:-6]), int(line[-4:-2])
        messages.append([x, y, dx, dy]) 

messages = np.array(messages)

print(messages)

for i in range(12000):
    for j, m in enumerate(messages):
        messages[j][0] += messages[j][2]
        messages[j][1] += messages[j][3]
    max_x, max_y = messages.max(axis=0)[:2]
    min_x, min_y = messages.min(axis=0)[:2]
    if not (max_x < 1000 and max_y < 1000 and min_x > 0 and min_y > 0):
        continue
    img = np.zeros((max_x+1, max_y+1))
    for m in messages:
        img[m[0], m[1]] = 1

    print(i+1)
    plt.imshow(img)
    plt.show()
