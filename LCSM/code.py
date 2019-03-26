
DNAs = []

with open('rosalind_lcsm.txt', 'r') as f:
    buf = f.readline().strip()
    while buf:
        name = buf[1:]
        DNA = ''
        buf = f.readline().strip()
        while buf and not buf.startswith('>'): 
            DNA += buf
            buf = f.readline().strip()
        DNAs.append(DNA)

import time
sta = time.time()
table = {}
for j in range(len(DNAs[0])):
    for k in range(j, len(DNAs[0])):
        table[DNAs[0][j:k+1]] = -1

# print(table)
for (i, dna) in enumerate(DNAs[1:]):
    # print(i,dna)
    for j in range(len(dna)):
        for k in range(j, len(dna)):
            if not dna[j:k+1] in table:
                break
            if table[dna[j:k+1]] < i - 1:
                # print(i)
                table.pop(dna[j:k+1])
                break
            else:
                # print(i, dna[j:k+1])
                table[dna[j:k+1]] = i
# print(table)

ans = ''
for item in table.items():
    if item[1] == len(DNAs)-2 and len(item[0]) > len(ans):
        ans = item[0]

print(ans)
end = time.time()
print('Time Cost: ' + str(end - sta) + 's')