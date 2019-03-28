
DNAs = []

with open('rosalind_tran.txt', 'r') as f:
    buf = f.readline().strip()
    while buf:
        name = buf[1:]
        DNA = ''
        buf = f.readline().strip()
        while buf and not buf.startswith('>'): 
            DNA += buf
            buf = f.readline().strip()
        DNAs.append(DNA)
        
changes = [(DNAs[0][i], DNAs[1][i]) for i in range(len(DNAs[0]))]
transition, transversion = 0, 0
for c in changes:
    if c[0] == c[1]:
        continue
    elif c in [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]:
        transition += 1
    else:
        transversion += 1

ratio = transition / transversion
print(ratio)
        
    