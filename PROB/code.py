import numpy as np

with open('rosalind_prob.txt', 'r') as f:
    buf = f.readlines()
    dna = buf[0].strip()
    A = buf[1].strip().split()

    for gc in A:
        gc = float(gc)
        p = np.log(0.5 * gc) * (dna.count('G') + dna.count('C')) + np.log(0.5*(1-gc)) * (dna.count('A') + dna.count('T'))
        print(p/np.log(10), end=' ')
    