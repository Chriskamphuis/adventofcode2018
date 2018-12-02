threes = 0
twos = 0

with open('input.txt') as f:
    for line in f:
        dic = {}
        for l in line:
            try: 
                dic[l] += 1
            except:
                dic[l] = 1
        a = [value for _, value in dic.items()]
        if 3 in a:
            threes += 1
        if 2 in a:
            twos += 1


print(threes * twos)
