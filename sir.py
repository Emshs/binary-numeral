import scipy.integrate as spi
import numpy as np
import pylab as pl 

beta = 0.1

gamma =  1/14 
t_inc = 1.0 
t_end = 150.0

S = 4950 ; I  = 50; R = 8

N = S + I + R
S  = 4950 /N  
I  = 50 /N    
R = 8 /N      

Input = (S, I, 0.0)

def simple_SIR(INT, t):
  Y=np.zeros((3))
  X = INT      #  S0,   I0 
  Y[0] = -beta * X[0] * X[1]
  Y[1] = beta*X[0]*X[1]  - gamma * X[1]
  Y[2] = gamma * X[1]
  return Y # for spicy.odeint

t_start =0.0 ; 
t_range = np.arange(t_start, t_end + t_inc, t_inc)
SIR= spi.odeint(simple_SIR, Input, t_range)

pl.figure(figsize=(15,8))
#pl.plot(SIR[:, 0], '-g', label='Susceptibles')
#pl.plot(SIR[:, 2], '-k', label='Recovereds')
pl.plot(SIR[:, 1], '-r', label='Infectious')
pl.legend(loc=0)
pl.title('Prediction of Simple H5N1 SIR(South Korea)')
pl.xlabel('Time(day)')
pl.ylabel('individuals')
pl.show()
