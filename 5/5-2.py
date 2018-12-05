import numpy as np

poly = ''

with open('input.txt') as f:
    poly = f.read()

units = {p.lower() for p in poly if p != '\n'}

def react(poly):
    i = 0
    while i < len(poly) - 1:
        if poly[i] == poly[i+1].lower() and poly[i] != poly[i+1]:
            poly = poly[:i] + poly[i+2:]
            i-=1
        elif poly[i].lower() == poly[i+1] and poly[i] != poly[i+1]:
            poly = poly[:i] + poly[i+2:]
            i-=1
        else:
            i+=1
    return i 

lowest = np.inf

for unit in units:
    low = unit
    high = unit.upper()
    poly_tmp = ''.join([p for p in poly if p != low and p != high])
    j = react(poly_tmp)
    if j < lowest:
        lowest = j

print(lowest) 
