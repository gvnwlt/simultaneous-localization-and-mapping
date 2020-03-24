#!/usr/bin/env python3 

p = [0.2] * 5 
world = ['green', 'red', 'red', 'green', 'green'] # ground truth 
measurements = ['red', 'green'] # Z 
pHit = 0.6 
pMiss = 0.2 

# receives input measurement of our world and then
# normalizes the input for hits and misses so that 
# our distribution adds to 1

# version 1 
#def sense(p, Z): 
#    q = [] # non-normalized distribution
#    # apply weights to observations 
#    for obs in world:
#        if obs == Z:
#            hit = p[world.index(obs)] * pHit
#            q.append(hit) 
#        else:
#            miss = p[world.index(obs)] * pMiss
#            q.append(miss)
#    # normalize the distribution 
#    qSum = sum(q)
#    for i in range(len(q)):-m 
#        q[i] = q[i] / qSum
#    return q 

# version 2 
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

red = sense(p,measurements[0])
green = sense(red, measurements[1])
print("prior distribution red: \n", red)
print("posterior distribution green: \n", green)
print("\ntotal probability: \n", sum(green))
