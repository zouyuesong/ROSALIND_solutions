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

names, DNAs = read_FASTA('revp')
dna = DNAs[0]

def find_reverse_palindrome(dna, length):
    def is_palindrome(string):
        from Bio.Seq import reverse_complement
        return string == reverse_complement(string)
        
        

    (l, r) = length
    for i in range(len(dna)):
        for j in range(l, min(len(dna)-i+1, r+1)):
            if is_palindrome(dna[i:i + j]):
                print(str(i+1) + ' ' + str(j))
                # print(dna[i:i+j])
                
# print(dna)
find_reverse_palindrome(dna, (4, 12))
    
