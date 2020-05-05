#!/usr/bin/env python3

import math

# gaussian model
def gaussian(mean, var, x):
    exp_0 = 1 / math.sqrt(2*math.pi*var)
    exp_1 = (x - mean)**2
    exp_2 = -1/2*(exp_1)
    exp_3 = exp_2 / var
    result = exp_0*(math.exp(exp_3))
    print(result)
    return result

# test
mean = 10
var = 4
x = 1

gaussian(mean, var, x)

