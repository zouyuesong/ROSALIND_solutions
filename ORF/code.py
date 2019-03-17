import Bio
from Bio.Seq import Seq, reverse_complement
from Bio.Alphabet import IUPAC

def translate(DNA):
    candidates = []
    for i in range(3, len(DNA)):
        if DNA[i - 3:i] == 'ATG':
            # print(i, DNA[i-3:])
            candidate = Seq(DNA[i-3:], IUPAC.unambiguous_dna).translate()
            p = candidate.find('*')
            if p != -1:
                candidate = str(candidate)[:p]
                candidates.append(candidate)
        
    DNA_rev = reverse_complement(DNA)
    for i in range(3, len(DNA)):
        if DNA_rev[i - 3:i] == 'ATG':
            # print(DNA[i-3:])
            candidate = Seq(DNA_rev[i-3:], IUPAC.unambiguous_dna).translate()
            p = candidate.find('*')
            if p != -1:
                candidate = str(candidate)[:p]
                candidates.append(candidate)

    return '\n'.join(list(set(candidates)))


if __name__ == "__main__":
    with open('rosalind_orf.txt', 'r') as f:
        DNA = ""
        lines = f.readlines()
        for line in lines[1:]: 
            DNA += line.rstrip('\n')
        # print(DNA)
        ans = translate(DNA)
        print(ans)