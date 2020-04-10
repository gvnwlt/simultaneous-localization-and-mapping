#!/usr/bin/env python3 

p = [0, 1, 0, 0, 0]
pExact = 0.8 
pUndershoot = 0.1
pOvershoot = 0.1 

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

print('current location: ', p)
for i in range(1000):
    p = move(p, 1)
print(p)