after_map = dict()
before_map = dict()
frontier = set()

with open('input.txt') as f:
    for line in f:
        before, after = line[5], line[-13] 
        frontier |= {before}
        frontier |= {after}
        try: 
            after_map[after] |= {before}
        except:
            after_map[after] = {before}
        try:
            before_map[before] |= {after}
        except:
            before_map[before] = {after}

elements = sorted(list(frontier)) 
frontier = frontier.difference(after_map.keys())
time = {elements[i] : i+61 for i in range(len(elements))}

i = 0
under_process = {}

while frontier != set() or len(under_process) > 0:
    released = [key for key, value in under_process.items() if value == i]      
    for rel in released:
        del under_process[rel]
        try:
            for value in before_map[rel]:
                after_map[value].remove(rel)
                if after_map[value] == set():
                    frontier |= {value}
        except:
            pass
    while frontier != set() and len(under_process) < 5:
        step = min(frontier)
        under_process[step] = i + time[step]
        frontier = frontier.difference(step)
    i+=1

print(i-1)
