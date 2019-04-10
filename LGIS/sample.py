with open('rosalind_lgis.txt', 'r') as f:
    n = int(f.readline())
    l = f.readline().strip().split(' ')

n = int(n)
l = list(map(int, l))

inc = [(0,[])]*(n+1)

for i in l:
    x,y = max(inc[:i])
    inc[i] = (x+1,y+[i])

print(" ".join(map(str,max(inc)[1])))