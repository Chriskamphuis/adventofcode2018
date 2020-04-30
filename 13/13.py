class Cart:
    def __init__(self, direction):
        self.direction = direction
        self.moved = False
    
    def next_turn(self):
        while True:
            for turn in ['left', 'straight', 'right']:
                yield turn

track = dict()
carts = dict()

with open('input.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line[:-1]):
            if c == ' ':
                continue
            elif c in ['-', '|', '\\', '/', '+']:
                track[(x, y)] = c
            elif c in ['>', '<']:
                track[(x, y)] = '-'
                if c == '>':
                    carts[(x, y)] = Cart('right')
                else:
                    carts[(x, y)] = Cart('left')
            elif c in ['^', 'v']:
                track[(x, y)] = '|'
                if c == '^':
                    carts[(x, y)] = Cart('up')
                else:
                    carts[(x, y)] = Cart('down')

for i in range(150):
    for j in range(150):
        cart = None
        try:
            cart = carts[(x, y)]
        except:
            continue
        
