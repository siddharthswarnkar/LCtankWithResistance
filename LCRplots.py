from __future__ import division
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import os


def odeSeriesHelper(initial,t,R,L,C):
    def odeSeriesInit(initial,t):
        initial_current = float(initial[0])
        initial_current_rate = float(initial[1])
        return [initial_current_rate, (-1/(L*C))*initial_current - (R/L)*initial_current_rate ]
    return odeSeriesInit
    
def odeParallelHelper(initial,t,R,L,C):
    def odeParallelInit(initial,t):
        initial_voltage = float(initial[0])
        initial_voltage_rate = float(initial[1])
        return [initial_voltage_rate, (-1/(L*C))*initial_voltage - (1/(R*C))*initial_voltage_rate ]
    return odeParallelInit

def odeStepResponseHelper(initial,t,R,L,C,Vs):
    def odeStepInit(initial,t):
        initial_voltage = float(initial[0])
        initial_voltage_rate = float(initial[1])
        return [initial_voltage_rate, Vs/(L*C) - initial_voltage/(L*C) - R*initial_voltage_rate/L]
    return odeStepInit

def LCRplots(func, initial, t, Title, legend):
    '''Plots all the relivant graphs of LCtankwithResistance
    with umderdamped, overdamped and critically damped case'''    
    ans = odeint(func, initial, t) 
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.plot(t,ans[:,0],'-bo',lw=1,label=legend[0])
    ax.hold('ON')
    ax.plot(t,ans[:,1],lw=1,label=legend[1])
    ax.set_xlabel('Time',family='sans-serif',style='italic',size=10)
    ax.set_title(Title,family='sans-serif',style='italic',size=10)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles,fontsize=10)
    #plt.savefig('somethin.png')
    plt.show()
    

#####################################        Source Free Series RLC        ########################################

########### for underdamped ####################
def plot_for_serial_underdamped():
    t = np.linspace(0,20,20)
    R=1
    L=1
    C=0.05        
    initial_current = 0
    initial_voltage = -1
    initial_current_rate = -(R*initial_current+initial_voltage)/float(L)
    initial = [initial_current,initial_current_rate]
    func = odeSeriesHelper(initial,t,R,L,C)
    LCRplots(func,initial,t,'Current and Rate of Currnet Across Inductor For Underdamped',['Current','Rate of Current'])

########## for critically damped ###############
def plot_for_serial_critical():
    t = np.linspace(0,20,1000)
    R=1
    L=1
    C=4
    initial_current = 0
    initial_voltage = -1
    initial_current_rate = -(R*initial_current+initial_voltage)/float(L)
    initial = [initial_current,initial_current_rate]
    func = odeSeriesHelper(initial,t,R,L,C)
    LCRplots(func,initial,t,'Current and Rate of Currnet Across Inductor For Critically Damped',['Current','Rate of Current'])

########## for overdamped #####################
def plot_for_serial_overdamped():
    t = np.linspace(0,20,1000)
    R=1
    L=1
    C=10
    initial_current = 0
    initial_voltage = -1
    initial_current_rate = -(R*initial_current+initial_voltage)/float(L)
    initial = [initial_current,initial_current_rate]
    func = odeSeriesHelper(initial,t,R,L,C)
    LCRplots(func,initial,t,'Current and Rate of Currnet Across Inductor For Overamped',['Current','Rate of Current'])

#####################################        Source Free Paralle RLC        ########################################

########### for underdamped ####################
def plot_for_parallel_underdamped():
    t = np.linspace(0,20,1000)
    R=1.0
    C=1.0
    L=0.05
    initial_voltage = 1
    initial_current = 0
    initial_voltage_rate = -(initial_voltage + R*initial_current)/float(R*C)
    initial = [initial_voltage, initial_voltage_rate]
    func = odeParallelHelper(initial,t,R,L,C)
    LCRplots(func,initial,t,'Voltage and Rate of Voltage Across Capacitor For Underdamped',['Voltage','Rate of Voltage'])

########## for critically damped ###############
def plot_for_parallel_critical():
    t = np.linspace(0,20,1000)
    R=1
    C=1
    L=4
    initial_voltage = 1
    initial_current = 0
    initial_voltage_rate = -(initial_voltage + R*initial_current)/float(R*C)
    initial = [initial_voltage, initial_voltage_rate]
    func = odeParallelHelper(initial,t,R,L,C)
    LCRplots(func,initial,t,'Voltage and Rate of Voltage Across Capacitor For Critically Damped',['Voltage','Rate of Voltage'])

########## for overdamped #####################
def plot_for_parallel_overdamped():
    t = np.linspace(0,20,1000)
    R=1
    C=1
    L=10
    initial_voltage = 1
    initial_current = 0
    initial_voltage_rate = -(initial_voltage + R*initial_current)/float(R*C)
    initial = [initial_voltage, initial_voltage_rate]
    func = odeParallelHelper(initial,t,R,L,C)
    LCRplots(func,initial,t,'Voltage and Rate of Voltage Across Capacitor For Overamped',['Voltage','Rate of Voltage'])

###############################  Step Response of RLC circuit  #######################################

def plot_for_step_underdamped():
    t = np.linspace(0,20,1000)
    Vs = 1.0
    R=1.0
    L=1.0
    C=0.05
    initial_voltage = 0
    initial_voltage_rate = 0
    initial = [initial_voltage, initial_voltage_rate]
    func = odeStepResponseHelper(initial,t,R,L,C,Vs)
    LCRplots(func,initial,t,'Step Response of Voltage and Rate of Voltage Across Capacitor For Underdamped',['Voltage','Rate of Voltage'])

def plot_for_step_critical():
    t = np.linspace(0,20,30)
    Vs = 1.0
    R=1.0
    L=1.0
    C=4.0
    initial_voltage = 0
    initial_voltage_rate = 0
    initial = [initial_voltage, initial_voltage_rate]
    func = odeStepResponseHelper(initial,t,R,L,C,Vs)
    LCRplots(func,initial,t,'Step Response of Voltage and Rate of Voltage Across Capacitor For Underdamped',['Voltage','Rate of Voltage'])

def plot_for_step_overdamped():
    t = np.linspace(0,40,1000)
    Vs = 1.0
    R=1.0
    L=1.0
    C=10.0
    initial_voltage = 0
    initial_voltage_rate = 0
    initial = [initial_voltage, initial_voltage_rate]
    func = odeStepResponseHelper(initial,t,R,L,C,Vs)
    LCRplots(func,initial,t,'Step Response of Voltage and Rate of Voltage Across Capacitor For Underdamped',['Voltage','Rate of Voltage'])

def main():
    
    #plot_for_serial_underdamped()
    #plot_for_parallel_underdamped()
    plot_for_step_critical()

if __name__ == '__main__':
    main()
