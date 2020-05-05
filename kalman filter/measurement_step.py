#!/usr/bin/env python3

# Description: Measurement step for Kalman filter 1D.

import math
#from gaussian import gaussian

# measurement_update: 
# - combine old Gaussian with the new Gaussian measurement
# to result in the posterior Gaussian values (mean, sig)
# -returns mean update and variance update
# -'sig' is short for sigma (the variance)
def measurement_update(mean, measurement, sig, measurement_sig):
    exp_1 = 1. / (sig + measurement_sig)
    exp_2 = ((measurement_sig*mean)+(sig*measurement))
    new_mean = exp_1 * exp_2

    exp_1 = 1. / sig
    exp_2 = 1. / measurement_sig
    new_sig = 1. / (exp_1 + exp_2)

    return [new_mean, new_sig]

# Test
#mean = 10
#measurement = 30
#sig = 8
#measurement_sig = 8
#measurement_update(mean, measurement, sig, measurement_sig)
