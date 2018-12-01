import sys

i = 0
a = {}
done = False
while True:
    with open('input.txt') as f:
        for line in f:
            try:
                k = a[i]
                print(i)
                done = True
                break
            except:
                a[i] = i 
                i += int(line[:-1])
    if done:
        break
