#!/usr/bin/env python3 

# 1. intializing belief 
p = []
n = 5 
pHit = 0.6
pMiss = 0.2 

for i in range(n):
    p.append(1. / n)

print('uniform distribution: \n', p, '\n')

# 2. probability grid hits and misses 
for i in range(n):
    if i == 1 or i == 2:
        p[i] = p[i] * pHit 
    else: 
        p[i] = p[i] * pMiss 

print('probability grid: \n', p, '\n')

# 3. sum of all values 
sum_p = sum(p)
print('sum of values: \n', sum_p, '\n')

# 4. now 'normalizing' the cells by dividing each cell by the sum 
for i in range(n):
    p[i] = p[i] / sum_p

# 5. sum of probability grid should always add to 1 -- validation 
sum_p = sum(p)
print('nomalized values: \n', p, '\n')
print('total of normalized distribution (should equal \'1\'): \n', sum_p)

