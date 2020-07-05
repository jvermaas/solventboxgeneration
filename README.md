# Solvetn Box Generation
Here are scripts and tools to generate solvent boxes suitable for use with the VMD solvate plugin.

## Prerequisites 

1. [charmm](https://www.charmm.org/charmm/showcase/news/free-charmm/), which is used to make the single solvent molecules. Single core version of charmm is fine, and is available for free for academics.
2. [GROMACS](http://manual.gromacs.org/documentation/), where we use the "insert-molecules" tool.
3. [psfgen and NAMD](https://www.ks.uiuc.edu/Development/Download/download.cgi), which are used to minimize the solvent box once assembled.

## Step-by-step instructions

```bash
python makesingle.py ; #Makes the single solvent molecule psf/pdb pairs
python makeboxes.py ; #Makes the boxes
python makesimdirs.py ; #Runs simulations to minimize and equilibrate the boxes.
```

There are a number of things that *can* go wrong in this process, but it works for me.
If you get margin violations, these aren't uncommon, since the box is initially too large, and shrinks alot in the beginning.
If this happens, make eq.namd simulate for a shorter time and restart, as the margin is reset on a restart.
