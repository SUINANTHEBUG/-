import perceval as pcvl
from perceval.rendering.circuit import SymbSkin, PhysSkin
import perceval.components.unitary_components as comp
import numpy as np


def gen_circuit(Phi_list): #Phi_list is a list of 30 values for the Phase Shifter parameters
    """
    Returns the generator as a Circuit -  no measurement yet
    """
    #next apply Phase shifters on to qubits 1-3, 0 index
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
