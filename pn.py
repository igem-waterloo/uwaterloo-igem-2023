def pn_dynamics(t, y): 
    pn, ppn = y
    nppn = 1/1.5 #average number of days required for development from prepupa to pupa in healthy plants
    npn = 1/2 #average number of days required for development from pupa to adult in healthy plants
    tpn = 0.2 #estimated daily death rates of pupae
    dpndt = nppn*ppn - (npn + tpn)*pn
    return [dpndt]