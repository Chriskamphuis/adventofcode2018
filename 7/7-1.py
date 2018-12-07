after_map = dict()
before_map = dict()
frontier = set()

with open('input.txt') as f:
    for line in f:
        before, after = line[5], line[-13] 
        frontier |= {before}
        try: 
            after_map[after] |= {before}
        except:
            after_map[after] = {before}
        try:
            before_map[before] |= {after}
        except:
            before_map[before] = {after}

frontier = frontier.difference(after_map.keys())
output = ''

while frontier != set():
    step = min(frontier)
    output += step
    frontier = frontier.difference({step})
    try:
        for value in before_map[step]:
            after_map[value].remove(step)
            if after_map[value] == set():
                frontier |= {value}
    except:
        pass

print(output)
