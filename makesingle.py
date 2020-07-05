#This script makes a single psf/pdb pair for a solvent molecule
#You'll need to set the resnames you want, and point the script to the topology and parameter files in the charmmscript.
import os
#CHARMM resnames for the solvent you want
resnames = ['AMM1', 'ACO', 'MEOH', 'ETOH', 'THF', 'HEXA', 'DMSO']
#The atom names for 3 connected atoms we will be using to "seed" positions
seeds = [['H11', 'N1', 'H12'], ['C2', 'C1', 'C3'], ['CB', 'OG', 'HG1'], ['C1', 'O1', 'HO1'], ["C1'", "O4'", "C4'"], ['C1', 'C2', 'C3'], ['C3', 'S2', 'C7']]

#resnames = ['OCOH']
#seeds = [['O1', 'C1', 'C2']]
for i, resname in enumerate(resnames):
	charmmscript = '''ioformat extended
read rtf card name top_all36_cgenff.rtf
bomlev -2
read para card name par_all36_cgenff.prm
bomlev 0
read sequence %s 1
generate ligm first none last none angle dihe setup
write psf card name singles/%s.psf
ic param
ic seed 1 %s 1 %s 1 %s
ic build
mini sd nstep 5000
write coor pdb name singles/%s.pdb
stop
''' % (resname.lower(), resname.lower(), seeds[i][0].lower(), seeds[i][1].lower(), seeds[i][2].lower(), resname.lower())
	fout = open("singles/%s.inp" % resname.lower(), "w")
	fout.write(charmmscript)
	fout.close()
	os.system("charmm < singles/%s.inp > singles/%s.log" % (resname.lower(), resname.lower()))
