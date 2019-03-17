bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

datafile = open('rosalind_mrna.txt','r')
prot = datafile.read()

number = 1
for aa in prot:
        number *= amino_acids.count(aa)
        number %= 1000000

print number * amino_acids.count('*') % 1000000