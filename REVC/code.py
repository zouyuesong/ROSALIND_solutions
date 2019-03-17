def revc(dna):
    dna_rev = dna[::-1]
    dna_rev = dna_rev.replace('A', 'a')
    dna_rev = dna_rev.replace('T', 'A')
    dna_rev = dna_rev.replace('a', 'T')
    dna_rev = dna_rev.replace('C', 'c')
    dna_rev = dna_rev.replace('G', 'C')
    dna_rev = dna_rev.replace('c', 'G')
    return dna_rev

if __name__ == "__main__":
    with open('rosalind_revc.txt', 'r') as f:
        dna = f.readlines()[0].rstrip('\n')
        dna_rev = revc(dna)
        print(dna_rev)


