#!/usr/bin/env python3 

# This program is the essence of Google's self-driving car
# where each program in the this directory starting with
# the uniform-distribution builds off of the previous to 
# assemble into these sense and move routines. 

# uniform prior distribution
p = [0.2] * 5 
# ground truth
world = [['red', 'red', 'green', 'red'],
         ['green', 'green', 'red'],
         ['red', 'red', 'green']]  
# measurement vector 
measurements = ['red', 'red', 'green'] # Z 
# motion vector
motions = [1, 1]
pHit = 0.6 
pMiss = 0.2 
pExact = 0.8 
pUndershoot = 0.1
pOvershoot = 0.1 

# Sense Function: sense when obstacles is detected and apply 
# probability to distribution when detected  
def sense(p, Z):
    q=[] # non-normalized distribution
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    # normalize the distribution 
    qSum = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / qSum
    return q

# Move Function: for movement 'U' if shift the values 'p' in the 
# grid over by that amount.  
# U <= -1 left 
# U >= 1 right 
def move(p, U): 
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
        
    return q

for i in range(len(measurements)):
    p = sense(p,measurements[i])
    p = move(p, motions[i])

print(p)