def l2t_dynamics(t, y):
    l2t, l1t = y
    nl2t = 1/2 #average number of days required for L2 to develop to prepupae in infected plants
    tl2t = 0.1 #estimated daily death rates of L2
    dl2tdt = nl2t*l1t - (nl2t + tl2t)*l2t
    return [dl2tdt]