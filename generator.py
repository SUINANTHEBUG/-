import perceval as pcvl
from perceval.rendering.circuit import SymbSkin, PhysSkin
import perceval.components.unitary_components as comp
import numpy as np



generator = pcvl.Circuit(4) #start off by intializing the circuit with 4 qubits
Phi_list = [np.pi] * 15 #modify this list to change the values

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
bs_2 = comp.BS.Ry() #again not sure which matrix
generator.add(1, bs_2)
bs_3 = comp.BS.Ry()
generator.add(0, bs_3)
bs_4 = comp.BS.Ry()
generator.add(2, bs_4)

#next is Phase shifters for qubits 0 and 2
ps5 = comp.PS(phi = Phi_list[4])
ps6 = comp.PS(phi = Phi_list[5])
generator.add(0, ps5)
generator.add(2, ps6)
#then beam splitters for 0 and 2
bs_5 = comp.BS.Ry()
bs_6 = comp.BS.Ry()
generator.add(0, bs_5)
generator.add(2, bs_6)
#next step one PS on 1
ps7 = comp.PS(phi = Phi_list[6])
generator.add(1, ps7)
#then BS on 1
bs_7  = comp.BS.Ry()
generator.add(1, bs_7)
#then PS on 1
ps8 = comp.PS(phi = Phi_list[7])
generator.add(1, ps8)
#then BS on 1
bs_8 = comp.BS.Ry()
generator.add(1, bs_8)
#then PS 0 and 2
ps9 = comp.PS(phi = Phi_list[8])
ps10 = comp.PS(phi = Phi_list[9])
generator.add(0, ps9)
generator.add(2, ps10)
#then BS on 0 and 2
bs_9 = comp.BS.Ry()
bs_10 = comp.BS.Ry()
generator.add(0, bs_9)
generator.add(2, bs_10)
#then PS 0 and 2
ps11 = comp.PS(phi = Phi_list[10])
ps12 = comp.PS(phi = Phi_list[11])
generator.add(0, ps11)
generator.add(2, ps12)
#then BS on 0 and 2
bs_11 = comp.BS.Ry()
bs_12 = comp.BS.Ry()
generator.add(0, bs_11)
generator.add(2, bs_12)
#then last is PS on 0-2
ps13 = comp.PS(phi = Phi_list[12])
ps14 = comp.PS(phi = Phi_list[13])
ps15 = comp.PS(phi = Phi_list[14])
generator.add(0, ps13)
generator.add(1, ps14)
generator.add(2, ps15)

#display circuit
pcvl.pdisplay(generator, skin=SymbSkin())
