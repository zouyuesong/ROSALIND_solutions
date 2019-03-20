import numpy as np 

dic = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
anti_dic = {0: 'A', 1: 'G', 2: 'C', 3: 'T'}

with open('rosalind_cons.txt', 'r') as f:
    buf = f.readline().strip()
    count = []
    DNA = ''
    buf = f.readline().strip()
    while not buf.startswith('>'): 
        DNA += buf
        buf = f.readline().strip()

    count = np.zeros((len(DNA), 4))
    for (i, c) in enumerate(DNA):
        count[i, dic[c]] = 1

    while buf:
        DNA = ''
        buf = f.readline().strip()
        while buf and not buf.startswith('>'): 
            DNA += buf
            buf = f.readline().strip()
        for (i, c) in enumerate(DNA): 
            count[i, dic[c]] += 1

    count = count.astype('int')
    mlca = ''
    for i in range(len(DNA)):
        mlca += anti_dic[np.argmax(count[i])]
    print(mlca)
    for c in range(4): 
        cc = anti_dic[c]
        print(cc + ':', end = ' ')
        for i in range(len(count)): 
            print(count[i][c], end=' ')
        print()
    
    
