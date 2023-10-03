def at_dynamics(t, y):
    at, pt = y 
    npt = 1/1.5 #average number of days required for development from pupa to adult in transmitter plants
    h = 791/800 #fraction of healthy plants
    tat = 1/(37.5 + 10.5*(2*h - 1)) #adults' life expectancy depending on the fraction of healthy plants available
    datdt = npt*pt - tat*at
    return [datdt]