def ppi_dynamics(t, y):
    ppi, l2i = y 
    nl2i = 1 #average number of days required for L2 to develop to prepupae in infected plants
    nppi = 1 #average number of days required for development from prepupa to pupa
    tppi = 0.1 #estimated daily death rates of prepupae
    dppidt = nl2i*l2i - (nppi + tppi)*ppi
    return [dppidt]