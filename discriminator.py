import perceval as pcvl
import perceval.components.unitary_components as comp
import numpy as np

## Use the symbolic skin for display
from perceval.rendering.circuit import DisplayConfig, SymbSkin, PhysSkin
from perceval.utils import StateVector
DisplayConfig.select_skin(PhysSkin)

sv = 0.5*(StateVector("|0, 0>") + StateVector("|1, 1>") + StateVector("|2, 2>") + StateVector("|3, 3>"))

print(sv.samples(10))

phi_discr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
discriminator = pcvl.Circuit(8)

discriminator.add(0, comp.PS(phi_discr[0])).add(1, comp.PS(phi_discr[1])).add(2, comp.PS(phi_discr[2]))
discriminator.add(4, comp.PS(phi_discr[3])).add(5, comp.PS(phi_discr[4])).add(6, comp.PS(phi_discr[5]))

discriminator.add((0, 1), comp.BS()).add((2,3), comp.BS())
discriminator.add((4, 5), comp.BS()).add((6,7), comp.BS())

discriminator.add(0, comp.PS(phi_discr[6])).add(2, comp.PS(phi_discr[7]))
discriminator.add(4, comp.PS(phi_discr[8])).add(6, comp.PS(phi_discr[9]))

discriminator.add((0, 1), comp.BS()).add((2,3), comp.BS())
discriminator.add((4, 5), comp.BS()).add((6,7), comp.BS())

discriminator.add((1, 2), comp.BS())
discriminator.add((5, 6), comp.BS())

discriminator.add(1, comp.PS(phi_discr[10]))
discriminator.add(5, comp.PS(phi_discr[11]))

pcvl.pdisplay(discriminator)


# phi = np.pi
# c = pcvl.Circuit(8)

# c.add(1, comp.PS(phi))
# c.add(2, comp.PS(phi))
# c.add(3, comp.PS(phi))
# c.add(5, comp.PS(phi))
# c.add(6, comp.PS(phi))
# c.add(7, comp.PS(phi))

# c.add((1, 2), comp.BS())
# c.add((5, 6), comp.BS())

# c.add(1, comp.PS(phi))
# c.add(5, comp.PS(phi))

# c.add((1, 2), comp.BS())
# c.add((5, 6), comp.BS())

# c.add((0, 1), comp.BS())
# c.add((2, 3), comp.BS())
# c.add((4, 5), comp.BS())
# c.add((6, 7), comp.BS())

# c.add(0, comp.PS(phi))
# c.add(2, comp.PS(phi))
# c.add(4, comp.PS(phi))
# c.add(6, comp.PS(phi))

# c.add((0, 1), comp.BS())
# c.add((2, 3), comp.BS())
# c.add((4, 5), comp.BS())
# c.add((6, 7), comp.BS())

# c.add(1, comp.PS(phi))
# c.add(5, comp.PS(phi))

# c.add((1, 2), comp.BS())
# c.add((5, 6), comp.BS())

# c.add(1, comp.PS(phi))
# c.add(5, comp.PS(phi))

# c.add((1, 2), comp.BS())
# c.add((5, 6), comp.BS())

# pcvl.pdisplay(c)
