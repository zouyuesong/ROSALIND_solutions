def find_motif(s, t):
    location = []
    for i in range(len(t), len(s)):
        if s[i - len(t):i] == t:
            location.append(i+1-len(t))
    return " ".join(str(i) for i in location)


if __name__ == "__main__":
    with open('rosalind_subs.txt', 'r') as f:
        lines = f.readlines()
        dna1 = lines[0].rstrip('\n')
        dna2 = lines[1].rstrip('\n')
        ans = find_motif(dna1, dna2)
        print(ans)