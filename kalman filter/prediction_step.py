#!/usr/bin/env python3

# Description: Prediction step for 1D Kalman filter. 

# prediction_update: 
# -produces offsets needed for mean and variance(sigma or 'sig')
# -returns the updated mean and variance (posterior distribution)
# -mean: the new mean calculated in the measurement step 
# -sig: variance is derived from the calculations in the measurement step
# in the measurement step 
def prediction_update(mean, motion, sig, motion_sig):
    return [(mean+motion), (sig+motion_sig)]
