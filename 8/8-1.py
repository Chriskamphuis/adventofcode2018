tree = []
with open('input.txt') as f:
    tree = [int(c) for c in f.read().strip().split(' ')]

def find_meta_data(score, tree):
    no_child_nodes, no_meta_data = tree[:2]
    tail = tree[2:]
    for n in range(no_child_nodes):
        score, tail = find_meta_data(score, tail)
    return score + sum(tail[:no_meta_data]), tail[no_meta_data:]

print(find_meta_data(0, tree)[0])
