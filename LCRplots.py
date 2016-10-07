from __future__ import division
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import os

def odeHelper(initial,t,R,L,C):
    initial_current = initial[0]
    initial_current_rate = initial[1]
    
    def odeInit(initial,t):
        return [initial_current_rate, (-1/L*C)*initial_current - (-R/L)*initial_current_rate ]

    return odeInit
    

def LCRplots(func, initial, t):
    '''Plots all the relivant graphs of LCtankwithResistance
    with umderdamped, overdamped and critically damped case'''
    
    current = odeint(func, initial, t)

    plt.plot(current, t)





if __name__ == '__main__':
    LCRplots()
