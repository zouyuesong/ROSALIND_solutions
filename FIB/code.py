def fib(n, k):
    F = [1, 1]
    for i in range(1, n):
        F.append(F[i] + F[i - 1] * k)
    # print(F)
    return F[n - 1]

if __name__ == "__main__":
    with open('rosalind_fib.txt', 'r') as f:
        l = f.readlines()[0].rstrip('\n')
        [n, k] = l.split()
        ans = fib(int(n), int(k))
        print(ans)
        