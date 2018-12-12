from collections import defaultdict

state = defaultdict(str)
rules = dict()

with open('input.txt') as f:
    initial_state = f.readline().strip().split()[-1]
    for i, c in enumerate(initial_state):
        state[i] = c
    _ = f.readline()
    for line in f.readlines():
        rule = line.strip().split()
        rules[rule[0]] = rule[2]

for generation in range(1, 201):
    new_state = defaultdict(str) 
    first_non_empty_pot = 0
        
    for k in range(min(state.keys())-2, max(state.keys())+2):
        key = "" 
        for j in range(k-2, k+3):
            if state[j] == '#':
                key += '#' 
            else: 
                key += '.'
        rule = rules[key]
        new_state[k] = rule

    for k in sorted(new_state.keys()):
        if new_state[k] == '.' and new_state[k+1] == '.' and new_state[k+2] == '.':
            del new_state[k]
        else:
            break


    old_state_string = ''.join([value for _, value in state.items()])
    old_state = state
    state = new_state
    state_string = ''.join([value for _, value in state.items()])

    if old_state_string == state_string:
        togo = 50000000000 - generation
                       
        old_total = 0
        for key, value in old_state.items():
            if value == '#':
                old_total += key
         
        total = 0
        for key, value in state.items():
            if value == '#':
                total += key
        print(total) 

        print(total + (togo * (total - old_total)))
        break
