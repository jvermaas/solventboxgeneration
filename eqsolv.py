import os
import subprocess
from atomsel import atomsel
from Molecule import Molecule
import numpy as np
resnames = ['ocoh']#['aco', 'bmim', 'dmso', 'etoh', 'hexa', 'meoh', 'thf']
for i, resname in enumerate(resnames):
	mol = Molecule()
	mol.load("%s/system.psf" % resname)
	mol.load("%s/run_0.dcd" % resname)
	sel = atomsel("all")
	minimum, maximum = sel.minmax()
	sel.moveby(-1 * np.array(minimum))
	sel.write("psf", "eqsolv/%s.psf" % resname)
	sel.write("pdb", "eqsolv/%s.pdb" % resname)
