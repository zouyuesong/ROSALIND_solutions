with open('rosalind_lexf.txt', 'r') as f:
    alphabet = f.readline().strip().split(' ')
    n = int(f.readline().rstrip('\n'))

    # print(symbol)
    # print(n**l)

import itertools 

for p in itertools.product(alphabet,repeat=n):
    print(''.join(p))