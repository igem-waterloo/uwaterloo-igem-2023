def ppn_dynamics(t, y): 
    ppn, l2h = y
    nl2h = 1/3 #average number of days required for L2 to develop to prepupae in healthy plants
    # l2h = l2hresults.l2h_dynamics(t, l2h) #amount of L2 in healthy plants
    nppn = 1/1.5 #average number of days required for development from prepupa to pupa in healthy plants
    tppn = 0.2 #estimated daily death rates for prepupae
    dppndt = nl2h*l2h - (nppn + tppn)*ppn
    return [dppndt]