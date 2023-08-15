import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import random

# Parameters
X = [0]    #initial population
t = [0]
k = 0.1 #growth rate
gamma = 0.05 #death rate

tend = 1000 #simulation end time

while t[-1] < tend:

        current_X = X[-1]

        rates = [k, gamma * current_X]
        rate_sum = sum(rates)

        tau = np.random.exponential(scale=1/rate_sum)   #tau is random draw from exponential distribution

        t.append(t[-1] + tau)

        rand = random.uniform(0,1)

        # growth event
        if rand * rate_sum > 0 and rand * rate_sum <= rates[0]:
                X.append(X[-1] + 1)

        # death event
        elif rand * rate_sum > rates[0] and rand * rate_sum <= rates[0] + rates[1]:
                X.append(X[-1] - 1)



plt.plot(t,X)
plt.xlabel("time")
plt.ylabel("eColi")
plt.show()
