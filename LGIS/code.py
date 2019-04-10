with open('rosalind_lgis.txt', 'r') as f:
    n = f.readline()
    seq = f.readline().strip().split(' ')

def find_longest_subsequence(seq, mode):
    if mode == 'inc':
        def comp(x, y):
            return x < y
    else:
        def comp(x, y):
            return x > y
    f = []


n = int(n)
seq = list(map(int, seq))
f_inc, fr_inc = [], []
f_dec, fr_dec = [], []
max_inc = 0
max_dec = 0
for (i, x) in enumerate(seq):
    t_inc = 0
    t_dec = 0
    fr_inc.append(-1)
    fr_dec.append(-1)
    for j in range(i):
        if seq[j] < x and t_inc < f_inc[j]:
            t_inc = f_inc[j]
            fr_inc[i] = j
        if seq[j] > x and t_dec < f_dec[j]:
            t_dec = f_dec[j]
            fr_dec[i] = j
    f_inc.append(t_inc+1)
    f_dec.append(t_dec+1)
    if f_inc[i] > f_inc[max_inc]:
        max_inc = i
    if f_dec[i] > f_dec[max_dec]:
        max_dec = i

subseq_inc = []
subseq_dec = []
while max_inc != -1:
    subseq_inc.append(seq[max_inc])
    max_inc = fr_inc[max_inc]
while max_dec != -1:
    # print(f_dec[max_dec])
    subseq_dec.append(seq[max_dec])
    max_dec = fr_dec[max_dec]

print(' '.join(list(map(str, subseq_inc[::-1]))))
print(' '.join(list(map(str, subseq_dec[::-1]))))

    

    
                