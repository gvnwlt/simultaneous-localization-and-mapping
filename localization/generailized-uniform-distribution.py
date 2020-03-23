#!/usr/bin/env python3

# This module represents a basic way to implement 
# a probability distribution. In this example the distribution 
# is not valid because it does not actually add up to '1'. 


# 1. probability of 5 places (uniform distribution)
p = [1] * 5

# 2. distribute the probability 
for i in range(len(p)):
    p[i] = p[i] / len(p)

print(p)

# to do another way
p = [] 
n = 5 

for i in range(n):
    p.append(1.0/n)

print(p)
