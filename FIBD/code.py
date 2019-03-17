def fib(n, m):
    F = [1, 1]
    T = [1, 0]
    for i in range(1, n):
        cur = F[i]
        new = F[i - 1]
        if i >= m-1:
            cur -= T[i - m + 1]
        if i >= m:
            new -= T[i - m]
        F.append(cur + new)
        T.append(new)
    # print(F)
    # print(T)
    return F[n - 1]

if __name__ == "__main__":
    with open('rosalind_fibd.txt', 'r') as f:
        l = f.readlines()[0].rstrip('\n')
        [n, m] = l.split()
        ans = fib(int(n), int(m))
        print(ans)
        
