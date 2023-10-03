import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import eh, et, l1h, l1t, l2h, l2i, l2t, ppn, ppi, ppt, pn, pi, pt, ai, an, at

def main():
    t_span = (0, 100)
    num_points = 100
    t_values = np.linspace(t_span[0], t_span[1], num_points)

    ## inital conditions ##
    eho = 6000
    eto = 108
    l1ho = 5760
    l1to = 99
    l2ho = 3000
    l2io = 0
    l2to = 45
    ppno = 0
    ppio = 0
    ppto = 0
    pno = 0
    pio = 0
    pto = 0
    ano = 1200
    aio = 310
    ato = 600

    ## results ##
    eh_values = [eho]
    et_values = [eto]
    l1h_values = [l1ho]
    l1t_values = [l1to]
    l2h_values = [l2ho]
    l2i_values = [l2io]
    l2t_values = [l2to]
    ppn_values = [ppno]
    ppi_values = [ppio]
    ppt_values = [ppto] 
    pn_values = [pno] 
    pi_values = [pio] 
    pt_values = [pto] 
    an_values = [ano] 
    ai_values = [aio] 
    at_values = [ato] 

    for t in t_values[1:]:
        eh_solution = solve_ivp(eh.eh_dynamics, (t-1, t), [eh_values[-1], at_values[-1], ai_values[-1], an_values[-1]], method='RK45')
        eh_values.append(eh_solution.y[0][-1])
        
        et_solution = solve_ivp(et.et_dynamics, (t-1, t), [et_values[-1], eh_values[-1], ai_values[-1], an_values[-1], at_values[-1]], method='RK45')
        et_values.append(et_solution.y[0][-1])

        l1h_solution = solve_ivp(l1h.l1h_dynamics, (t-1, t), [l1h_values[-1], eh_values[-1], ai_values[-1], an_values[-1], at_values[-1]], method='RK45')
        l1h_values.append(l1h_solution.y[0][-1])

        l1t_solution = solve_ivp(l1t.l1t_dynamics, (t-1, t), [l1t_values[-1], l1h_values[-1], et_values[-1], ai_values[-1], an_values[-1], at_values[-1]], method='RK45')
        l1t_values.append(l1t_solution.y[0][-1])

        l2h_solution = solve_ivp(l2h.l2h_dynamics, (t-1, t), [l2h_values[-1], l1h_values[-1], ai_values[-1], an_values[-1], at_values[-1]], method='RK45')
        l2h_values.append(l2h_solution.y[0][-1])

        l2t_solution = solve_ivp(l2t.l2t_dynamics, (t-1, t), [l2t_values[-1], l1t_values[-1]], method='RK45')
        l2t_values.append(l2t_solution.y[0][-1])

        l2i_solution = solve_ivp(l2i.l2i_dynamics, (t-1, t), [l2i_values[-1], l2h_values[-1], ai_values[-1], an_values[-1], at_values[-1]], method='RK45')
        l2i_values.append(l2i_solution.y[0][-1])

        ppn_solution = solve_ivp(ppn.ppn_dynamics, (t-1, t), [ppn_values[-1], l2h_values[-1]], method='RK45')
        ppn_values.append(ppn_solution.y[0][-1])

        ppi_solution = solve_ivp(ppi.ppi_dynamics, (t-1, t), [ppi_values[-1], l2i_values[-1]], method='RK45')
        ppi_values.append(ppi_solution.y[0][-1])

        ppt_solution = solve_ivp(ppt.ppt_dynamics, (t-1, t), [ppt_values[-1], l2t_values[-1]], method='RK45')
        ppt_values.append(ppt_solution.y[0][-1])

        pn_solution = solve_ivp(pn.pn_dynamics, (t-1, t), [pn_values[-1], ppn_values[-1]], method='RK45')
        pn_values.append(pn_solution.y[0][-1])

        pi_solution = solve_ivp(pi.pi_dynamics, (t-1, t), [pi_values[-1], ppi_values[-1]], method='RK45')
        pi_values.append(pi_solution.y[0][-1])

        pt_solution = solve_ivp(pt.pt_dynamics, (t-1, t), [pt_values[-1], ppt_values[-1]], method='RK45')
        pt_values.append(pt_solution.y[0][-1])

        an_solution = solve_ivp(an.an_dynamics, (t-1, t), [an_values[-1], pn_values[-1]], method='RK45')
        an_values.append(an_solution.y[0][-1])

        ai_solution = solve_ivp(ai.ai_dynamics, (t-1, t), [ai_values[-1], an_values[-1], pi_values[-1]], method='RK45')
        ai_values.append(ai_solution.y[0][-1])

        at_solution = solve_ivp(at.at_dynamics, (t-1, t), [at_values[-1], pt_values[-1]], method='RK45')
        at_values.append(at_solution.y[0][-1])

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.plot(t_values, eh_values, label='Healthy plants') 
    plt.plot(t_values, et_values, label='Infected plants')
    plt.xlabel('Time')
    plt.ylabel('Amount of Eggs') 
    plt.legend(loc='upper left')
    plt.title('Egg Dynamics')

    plt.subplot(2, 3, 2)
    plt.plot(t_values, l1h_values, label='Healthy plants')
    plt.plot(t_values, l1t_values, label='Infected plants')
    plt.xlabel('Time')
    plt.ylabel('Amount of Larvae 1')
    plt.legend(loc='upper left')
    plt.title('Larvae 1 Dynamics')

    plt.subplot(2, 3, 3)
    plt.plot(t_values, l2h_values, label='Healthy plants')
    plt.plot(t_values, l2t_values, label='Infected plants')
    plt.plot(t_values, l2i_values, label='Newly infected plants')
    plt.xlabel('Time')
    plt.ylabel('Amount of Larvae 2')
    plt.legend(loc='upper left')
    plt.title('Larvae 2 Dynamics')

    plt.subplot(2, 3, 4)
    plt.plot(t_values, ppn_values, label='Non-infected')
    plt.plot(t_values, ppt_values, label='Future transmitters')
    plt.plot(t_values, ppi_values, label='Infected')
    plt.xlabel('Time')
    plt.ylabel('Amount of Pre-pupae')
    plt.legend(loc='upper left')
    plt.title('Pre-Pupae Dynamics')

    plt.subplot(2, 3, 5)
    plt.plot(t_values, pn_values, label='Non-infected')
    plt.plot(t_values, pt_values, label='Transmitter')
    plt.plot(t_values, pi_values, label='Infected')
    plt.xlabel('Time')
    plt.ylabel('Amount of Pupae')
    plt.legend(loc='upper left')
    plt.title('Pupae Dynamics')

    plt.subplot(2, 3, 6)
    plt.plot(t_values, an_values, label='Non-infected')
    plt.plot(t_values, at_values, label='Transmitter')
    plt.plot(t_values, ai_values, label='Infected')
    plt.xlabel('Time') 
    plt.ylabel('Amount of F. occidentalis adults')
    plt.legend(loc='upper left')
    plt.title('Adult Dynamics')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
