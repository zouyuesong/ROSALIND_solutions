import numpy as np

def Hamming_dist(s, t):
    return sum(np.array([s[i]!=t[i] for i in range(len(s))]))

with open('rosalind_hamm.txt', 'r') as f:
    [s, t] = f.readlines()
    s = s.rstrip('\n')
    t = t.rstrip('\n')
    ans = Hamming_dist(s, t)
    print(ans)
