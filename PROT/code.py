import Bio
from Bio.Seq import Seq
def translate(mRNA):
    return Seq(mRNA).translate().rstrip('*')

if __name__ == "__main__":
    with open('rosalind_prot.txt', 'r') as f:
        l = f.readlines()[0].rstrip('\n')
        ans = translate(l)
        print(ans)