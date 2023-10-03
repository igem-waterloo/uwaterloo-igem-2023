def pt_dynamics(t, y):  
    pt, ppt = y
    nppt = 1/1 #average number of days required for development from prepupa to pupa in transmitter plants
    npt = 1/1.5 #average number of days required for development from pupa to adult in transmitter plants
    tpt = 0.1 #estimated daily death rates of pupae
    dptdt = nppt*ppt - (npt + tpt)*pt
    return [dptdt]