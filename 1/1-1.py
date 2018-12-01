i = 0
with open('input.txt') as f:
    for line in f:
        i += int(line[:-1])
print(i)
