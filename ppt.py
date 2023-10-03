def ppt_dynamics(t, y): 
    ppt, l2t = y
    nl2t = 1 #average number of days required for L2 to develop to prepupae in infected plants
    nppt = 1 #average number of days required for development from prepupa to pupa
    tppt = 0.1 #estimated daily death rates of prepupae
    dpptdt = nl2t*l2t - (nppt + tppt)*ppt
    return [dpptdt]