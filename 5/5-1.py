import numpy as np

poly = ''

with open('input.txt') as f:
    poly = f.read()

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

print(i) 
