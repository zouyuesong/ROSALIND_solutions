with open('rosalind_iprb.txt', 'r') as f:
    [k, m, n] = f.readlines()[0].strip().split()
    k = int(k)
    m = int(m)
    n = int(n)
    p = (k * (k - 1) + 2 * k * (m + n) + m * (m - 1) * 3 / 4 + m * n) / (k + m + n) / (k + m + n - 1)
    print(p)
