import MDAnalysis as mda
from sys import argv

myinput = str(argv[1])

u = mda.Universe(myinput)

Bilayer = u.select_atoms('resname DOPG DOPE')
Bilayer_Protein = u.select_atoms('(resname DOPG DOPE) or protein')
Solvent = u.select_atoms('resname W or name NA CL')

with mda.selections.gromacs.SelectionWriter('index.ndx', mode='a') as ndx:
    ndx.write(Bilayer, name="Bilayer")
    ndx.write(Bilayer_Protein, name="Bilayer_Protein")
    ndx.write(Solvent, name="Solvent")
