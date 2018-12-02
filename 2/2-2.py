import numpy as np

with open('input.txt') as f:
    a = [l[:-1] for l in f]
for line in a:
    for k in a:
        line = np.array([l for l in line])
        k = np.array([j for j in k])
        if (line == k).all():
            continue
        out = np.array([line != k], dtype=bool)
        if np.sum(out) == 1:
            done = ''
            for i in line[line == k]:
                done += i
            print(done)
