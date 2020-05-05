#!/usr/bin/env python3

# Description: This is a full Kalman filter for 1D. 

from measurement_step import measurement_update
from prediction_step import prediction_update

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurements_sig = 4. 
motion_sig = 2.
mu = 0.
sig = 0.000000000001

N = len(measurements)

# Test: calculates the bot's position given by previous and new distributions from 
# the measurement step  
for i in range(N):
    [mu, sig] = measurement_update(mu, measurements[i], sig, measurements_sig)
    print('update: ', [mu, sig])
    [mu, sig] = prediction_update(mu, motion[i], sig, motion_sig)
    print('prediction: ', [mu, sig])