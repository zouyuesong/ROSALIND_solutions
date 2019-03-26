from scipy.special import comb

with open('rosalind_lia.txt') as f:
    (k, N) = f.readline().strip().split()
    k = int(k)
    N = int(N)
    n = 2**k

    
    prob = 0
    for i in range(N, n+1): 
        prob += comb(n, i) * 3**(n-i)
    prob /= 4 ** n
    print(prob)
    
    