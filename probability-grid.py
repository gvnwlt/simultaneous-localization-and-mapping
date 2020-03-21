#!/usr/bin/env python 

# intializing belief 
p = []
n = 5 

for i in range(n):
    p.append(1. / n)

print('uniform distribution: \n', p)

# probability grid hits and misses 
for i in range(n):
    if i == 1 or i == 2: # hit
        p[i] = p[i] * 0.6 
    else: 
        p[i] = p[i] * 0.2 # miss 

print('probability grid: \n', p)

# sum of all values 
print('sum of values: \n', sum(p))