def scan_DNA(f, buf):
    name = buf[1:]
    DNA = ''
    buf = f.readline().strip()
    while buf and not buf.startswith('>'): 
        DNA += buf
        buf = f.readline().strip()
    return name, DNA, buf
        

with open('rosalind_splc.txt', 'r') as f:
    buf = f.readline().strip()
    _, dna, buf = scan_DNA(f, buf)
    introns = []
    while buf:
        _, intron, buf = scan_DNA(f, buf)
        introns.append(intron)

from Bio.Seq import Seq
def transcribe(DNA):
    return Seq(DNA).translate().rstrip('*')

protein = ''
i = 0
while i < len(dna):
    is_intron = 1
    while is_intron:
        is_intron = 0
        for intron in introns:
            if dna[i:i + len(intron)] == intron:
                i += len(intron)
                is_intron = 1
    protein += transcribe(dna[i:i+3])
    i += 3

print(protein)
    