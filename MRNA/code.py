def infer(protein, mod=int(1e6)):
    ans = 3
    infer_dict = {'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1, 'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2, 'H': 2, 'N': 2, 'D': 2, 'Q': 2, 'K': 2, 'E': 2, 'C': 2, 'R': 6, 'G': 4, 'W': 1}
    for p in protein:
        ans = (ans * infer_dict[p]) % mod
    return ans

if __name__ == "__main__":
    with open('rosalind_mrna.txt', 'r') as f:
        l = f.readlines()[0].rstrip('\n')
        ans = infer(l)
        print(ans)
        