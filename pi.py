def pi_dynamics(t, y): 
    pi, ppi = y
    nppi = 1/1 #average number of days required for development from prepupa to pupa in infected plants
    npi = 1/1.5 #average number of days required for development from pupa to adult in infected plants
    tpi = 0.1 #estimated daily death rates of pupae
    dpidt = nppi*ppi - (npi + tpi)*pi
    return [dpidt]