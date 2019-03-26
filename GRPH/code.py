

nodes = []

with open('rosalind_grph.txt', 'r') as f:
    buf = f.readline().strip()
    while buf:
        name = buf[1:]
        DNA = ''
        buf = f.readline().strip()
        while buf and not buf.startswith('>'): 
            DNA += buf
            buf = f.readline().strip()
        nodes.append((name, DNA))

for u in nodes:
    for v in nodes: 
        if u != v and u[1][-3:] == v[1][:3]:
            print(u[0] + ' ' + v[0])
