import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

#Parameters
N0 = 10 ** (3) 
N_0 = [N0] #inoculum size (cfu/ml)
t = np.linspace(0, 12, num = 1000)
r = 2.1 #growth rate (can be function of temperature) (but not for our purposes) (1/hr)
k = 0.69 #adjustment factor (note this is c in the referenced paper)
N_min = (1 - (1/ (10 ** 6)))*N0 # Minimum population, 1ppm smaller than N_0 (cfu/ml)
N_max = 10 ** (8.9) # Maximum populatiaon (cfu/ml)

params = [r, k, N_min, N_max]

# Logistic growth equation
def sim(var, t, params):
    N = var[0]
    r = params[0]
    k = params[1]
    N_min = params[2]
    N_max = params[3]

    dNdt = r*N*(1 - (N / N_max))* ((1 - (N_min / N))**k)

    return ([dNdt])

#Solving the ODE
y = odeint(sim, N_0, t, args=(params,))

#Create plot
log_y = np.log10(y)
plt.plot(t, y[:,0])
plt.xlabel("Time(h)")
plt.ylabel("log N (cfu/ml)")
plt.show()

