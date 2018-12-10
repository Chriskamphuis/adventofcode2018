tree = []
with open('input.txt') as f:
    tree = [int(c) for c in f.read().strip().split(' ')]

def find_meta_data(tree):
    no_child_nodes, no_meta_data = tree[:2]
    tail = tree[2:]
    if no_child_nodes == 0:
        return sum(tail[:no_meta_data]), tail[no_meta_data:]
    scores = []
    out = 0
    for n in range(no_child_nodes):
        s, tail = find_meta_data(tail)
        scores.append(s) 
    for n in range(no_meta_data):
        try:
            out += scores[tail[n]-1]
        except:
            pass
    return out, tail[no_meta_data:]

print(find_meta_data(tree)[0])
