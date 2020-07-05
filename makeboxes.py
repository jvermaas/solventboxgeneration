#This script uses the insert-molecules tool to take the single molecules and put 1000 of them in a box.
#psfgen then makes a psf. You'll need to change the topology location, and have psfgen in your path.
import os
import subprocess
resnames = ['AMM1', 'ACO', 'MEOH', 'ETOH', 'THF', 'HEXA', 'DMSO']
#resnames = ['OCOH']
#Make this directory first.
os.chdir("boxes")
for i, resname in enumerate(resnames):
	realname = resname.lower()
	subprocess.call("gmx insert-molecules -ci ../singles/%s.pdb -o %s.pdb -nmol 1000 -box 8.2 8.2 8.2" % (realname, realname), shell=True)
	fout = open("tmp.psfgen", "w")
	fout.write('''topology ../top_all36_cgenff.rtf
segment QQQ {
	for { set i 0 } { $i < 1000 } { incr i } {
		residue $i %s
	}
}
regenerate angles dihedrals
writepsf %s.psf
''' % (realname, realname))
	fout.close()
	subprocess.call("psfgen < tmp.psfgen", shell=True)

# subprocess.call("gmx insert-molecules -ci ../singles/bmim.pdb -o bmim.pdb -nmol 500 -box 8 8 8" , shell=True)
# fout = open("tmp.psfgen", "w")
# fout.write('''topology ../toppar/bmim.top
# segment QQQ {
# 	for { set i 0 } { $i < 500 } { incr i } {
# 		residue $i BMIM
# 	}
# 	for { set i 500 } { $i < 1000 } { incr i } {
# 		residue $i CLA
# 	}
# }
# regenerate angles dihedrals
# writepsf bmim.psf
# ''')
# fout.close()
# subprocess.call("psfgen < tmp.psfgen", shell=True)
# from Molecule import Molecule
# from atomsel import atomsel
# import numpy as np
# oldmol = Molecule()
# oldmol.load("bmim.pdb")
# oldsel = atomsel("all")
# newmol = Molecule()
# newmol.load("bmim.psf")
# newmol.dupFrame()
# newsel = atomsel("serial 1 to %d" % len(oldsel))
# for el in ['x', 'y', 'z']:
# 	newsel.set(el, oldsel.get(el))
# newsel2 = atomsel("index > %d" % len(oldsel))
# sodpos = np.random.rand(len(newsel2), 3) * 80
# for i, el in enumerate(['x', 'y', 'z']):
# 	newsel2.set(el, sodpos[:,i])
# newmol.save("bmim.pdb")
exit()
