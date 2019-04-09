
def read_FASTA(File):
    names, DNAs = [], []
    with open('rosalind_'+File+'.txt', 'r') as f:
        buf = f.readline().strip()
        while buf:
            name = buf[1:]
            DNA = ''
            buf = f.readline().strip()
            while buf and not buf.startswith('>'): 
                DNA += buf
                buf = f.readline().strip()
            names.append(name)
            DNAs.append(DNA)
        return names, DNAs


import Bio
from Bio import Seq
