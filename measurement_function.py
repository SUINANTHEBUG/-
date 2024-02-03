import perceval as pcvl
import numpy as np
from scipy.optimize import minimize
import perceval.components.unitary_components as comp

## Use the symbolic skin for display
from perceval.rendering.circuit import DisplayConfig, SymbSkin
from perceval.utils import StateVector
DisplayConfig.select_skin(SymbSkin)


def g_objective(theta_g,theta_d):
    """
    Accepts two 1D np arrays corresponding to generator and discriminator parameters and returns a measurement of distance between gen and target
    """
    theta_g = theta_g.tolist()
    theta_d = theta_d.tolist()

    init = pcvl.BasicState("|1, 0, 0, 0, 1, 0, 0, 0>") + pcvl.BasicState("|0, 1, 0, 0, 0, 1, 0, 0>") + pcvl.BasicState("|0, 0, 1, 0, 0, 0, 1, 0>") + pcvl.BasicState("|0, 0, 0, 1, 0, 0, 0, 1>")
    target = pcvl.BasicState("|1,0,0,0,0,1,0,0>")+pcvl.BasicState("|0,1,0,0,0,0,1,0>")+pcvl.BasicState("|0,0,1,0,0,0,0,1>")+pcvl.BasicState("|0,0,0,1,1,0,0,0>")

    generator = make_generator(theta_g)
    discriminator = make_discriminator(theta_d)

    # combine gen and discr into one circuit
    full = pcvl.Circuit(8).add(0, generator, merge=True).add(0, discriminator, merge=True)

    prob_22_init = measure(full, init) # measurement of generated state
    prob_22_target = measure(discriminator, target) # measurement of target state

    return abs(prob_22_target - prob_22_init) # compare generated and target states

def measure(circuit, state):
    """
    Accepts a circuit and a state. Runs the state through the circuit & retrieves probability
    distribution, then returns the value for |2, 2>
    """
    backend = pcvl.BackendFactory.get_backend("SLOS")

    sim = pcvl.Simulator(backend)
    sim.set_circuit(circuit)

    distr = sim.probs_svd(pcvl.SVDistribution(sim.evolve(state)))["results"]
    return list(distr.items())[2][1]


def make_generator(Phi_list): #Phi_list is a list of 30 values for the Phase Shifter parameters
    """
    Takes in list of angles. Returns the generator as a Circuit.
    """
    generator = pcvl.Circuit(8)
    BS = comp.BS()

    #next apply Phase shifters on to qubits 1-3, 0 index
    ps1 = comp.PS(phi = Phi_list[0]) # these may have to be variables and change
    ps2 = comp.PS(phi = Phi_list[1])
    ps3 = comp.PS(phi = Phi_list[2])
    generator.add(1, ps1) #add to second qubit
    generator.add(2, ps2)
    generator.add(3, ps3)

    # next is a beam splitter, or matrix applied to bits 1 and 2
    bs_1 = comp.BS() #not sure which matrix
    generator.add(1, bs_1)

    # after is another step of rotating
    ps4 = comp.PS(phi = Phi_list[3])
    generator.add(1, ps4)
    # then another beam splitter
    bs_2 = comp.BS() #again not sure which matrix
    generator.add(1, bs_2)
    bs_3 = comp.BS()
    generator.add(0, bs_3)
    bs_4 = comp.BS()
    generator.add(2, bs_4)

    #next is Phase shifters for qubits 0 and 2
    ps5 = comp.PS(phi = Phi_list[4])
    ps6 = comp.PS(phi = Phi_list[5])
    generator.add(0, ps5)
    generator.add(2, ps6)
    #then beam splitters for 0 and 2
    bs_5 = comp.BS()
    bs_6 = comp.BS()
    generator.add(0, bs_5)
    generator.add(2, bs_6)
    #next step one PS on 1
    ps7 = comp.PS(phi = Phi_list[6])
    generator.add(1, ps7)
    #then BS on 1
    bs_7  = comp.BS()
    generator.add(1, bs_7)
    #then PS on 1
    ps8 = comp.PS(phi = Phi_list[7])
    generator.add(1, ps8)
    #then BS on 1
    bs_8 = comp.BS()
    generator.add(1, bs_8)
    #then PS 0 and 2
    ps9 = comp.PS(phi = Phi_list[8])
    ps10 = comp.PS(phi = Phi_list[9])
    generator.add(0, ps9)
    generator.add(2, ps10)
    #then BS on 0 and 2
    bs_9 = comp.BS()
    bs_10 = comp.BS()
    generator.add(0, bs_9)
    generator.add(2, bs_10)
    #then PS 0 and 2
    ps11 = comp.PS(phi = Phi_list[10])
    ps12 = comp.PS(phi = Phi_list[11])
    generator.add(0, ps11)
    generator.add(2, ps12)
    #then BS on 0 and 2
    bs_11 = comp.BS()
    bs_12 = comp.BS()
    generator.add(0, bs_11)
    generator.add(2, bs_12)
    #then last is PS on 0-2
    ps13 = comp.PS(phi = Phi_list[12])
    ps14 = comp.PS(phi = Phi_list[13])
    ps15 = comp.PS(phi = Phi_list[14])
    generator.add(0, ps13)
    generator.add(1, ps14)
    generator.add(2, ps15)

    ### next layer
    generator.add(5, comp.PS(phi = Phi_list[15])) #add to second qubit
    generator.add(6, comp.PS(phi = Phi_list[16]))
    generator.add(7, comp.PS(phi = Phi_list[17]))

    # next is a beam splitter, or matrix applied to bits 1 and 2
    generator.add(5, comp.BS())

    # after is another step of rotating
    ps4 = comp.PS(phi = Phi_list[3])
    generator.add(5, comp.PS(phi = Phi_list[18]))
    # then another beam splitter
    generator.add(5, comp.BS())
    generator.add(4, BS)
    generator.add(6, BS)

    #next is Phase shifters for qubits 0 and 2
    generator.add(4, comp.PS(phi = Phi_list[19]))
    generator.add(6, comp.PS(phi = Phi_list[20]))
    #then beam splitters for 0 and 2

    generator.add(4, BS)
    generator.add(6, BS)
    #next step one PS on 1
    generator.add(5, comp.PS(phi = Phi_list[21]))
    #then BS on 1
    generator.add(5, BS)
    #then PS on 1
    generator.add(5, comp.PS(phi = Phi_list[22]))
    #then BS on 1
    generator.add(5, BS)
    #then PS 0 and 2
    ps9 = comp.PS(phi = Phi_list[8])
    ps10 = comp.PS(phi = Phi_list[9])
    generator.add(4, comp.PS(phi = Phi_list[23]))
    generator.add(6, comp.PS(phi = Phi_list[24]))
    #then BS on 0 and 2
    generator.add(4, BS)
    generator.add(6, BS)
    #then PS 0 and 2
    ps11 = comp.PS(phi = Phi_list[10])
    ps12 = comp.PS(phi = Phi_list[11])
    generator.add(4, comp.PS(phi = Phi_list[25]))
    generator.add(6, comp.PS(phi = Phi_list[26]))
    #then BS on 0 and 2
    generator.add(4, BS)
    generator.add(6, BS)
    #then last is PS on 0-2
    generator.add(4, comp.PS(phi = Phi_list[27]))
    generator.add(5, comp.PS(phi = Phi_list[28]))
    generator.add(6, comp.PS(phi = Phi_list[29]))

    return generator


def d_objective(theta_d,theta_g):
    """Accepts two 1D np arrays corresponding to discriminator and generator parameters and returns a negative measurement of distance between gen and target"""
    return -g_objective(theta_g, theta_d)

num_rounds = 200
theta_d,theta_g = np.array([]),np.array([])

for i in range(num_rounds):
    best_generator = minimize(g_objective, theta_g, method='nelder-mead', args = (theta_d), options={'xatol': 1e-8, 'disp': True})
    theta_g = best_generator.x
    best_discriminator = minimize(d_objective, theta_d, method='nelder-mead', args = (theta_g), options={'xatol': 1e-8, 'disp': True})
    theta_d = best_discriminator.x

def make_discriminator(phi_list):
    """
    Takes in list of angles. Returns the discriminator as a Circuit.
    """
    discriminator = pcvl.Circuit(8) # initialize circuit w/ 8 qubits

    # first column of gates: PS 0, 1, 2, 4, 5, 6
    discriminator.add(0, comp.PS(phi_list[0])).add(1, comp.PS(phi_list[1])).add(2, comp.PS(phi_list[2]))
    discriminator.add(4, comp.PS(phi_list[3])).add(5, comp.PS(phi_list[4])).add(6, comp.PS(phi_list[5]))

    # second column of gates: BS 0-1, 2-3, 4-5, 6-7
    discriminator.add((0, 1), comp.BS()).add((2,3), comp.BS())
    discriminator.add((4, 5), comp.BS()).add((6,7), comp.BS())

    # third column of gates: PS 0, 2, 4, 6
    discriminator.add(0, comp.PS(phi_list[6])).add(2, comp.PS(phi_list[7]))
    discriminator.add(4, comp.PS(phi_list[8])).add(6, comp.PS(phi_list[9]))

    # third column of gates: BS 0-1, 2-3, 4-5, 6-7
    discriminator.add((0, 1), comp.BS()).add((2,3), comp.BS())
    discriminator.add((4, 5), comp.BS()).add((6,7), comp.BS())

    # fourth column of gates: BS 1-2, 5-6
    discriminator.add((1, 2), comp.BS())
    discriminator.add((5, 6), comp.BS())

    # fifth column of gates: PS 1, 5
    discriminator.add(1, comp.PS(phi_list[10]))
    discriminator.add(5, comp.PS(phi_list[11]))

    return discriminator

# test with random values
# print(g_objective([0, 0, 0, 0.1, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0], [0, 0.2, 0, 0.5, 0, 0, 0, 0.8, 0, 0, 0.9, 0]))
