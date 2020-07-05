import os
def mymkdir(s):
	if not os.path.exists(s):
		os.makedirs(s)
def mysymlink(source, dest):
	#print source, dest
	if not os.path.exists(dest):
		os.symlink(source, dest)
resnames = ['ACO', 'MEOH', 'ETOH', 'THF', 'HEXA', 'DMSO']
#resnames = ['OCOH']
import subprocess
for res in resnames:
	name = res.lower()
	mymkdir(name)
	os.chdir(name)
	mysymlink("../eq.namd", "eq.namd")
	mysymlink("../boxes/%s.psf" % name, "system.psf")
	mysymlink("../boxes/%s.pdb" % name, "system.pdb")
	subprocess.call(" ~/NAMD_2.13_Linux-x86_64-multicore-CUDA/namd2 +p8 eq.namd | tee eq.log", shell=True)
	os.chdir("..")
