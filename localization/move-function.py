#!/usr/bin/env python3 

p = [0, 1, 0, 0, 0]
pHit = 0.6 
pMiss = 0.2 

# Move Function: for movement 'U' if shift the values 'p' in the 
# grid over by that amount.  
# U <= -1 left 
# U >= 1 right 
def move(p, U): 
    q = []
    for i in range(len(p)):
        q.append(p[(i-U) % len(p)])
    return q

print('current location: ', p)
print('new location:     ', move(p, 4))