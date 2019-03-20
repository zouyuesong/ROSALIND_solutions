from Bio import SeqIO
from Bio.SeqUtils import GC
GCcont = 0
GCname = ""
file = open("rosalind_GC.txt", "r")
for record in SeqIO.parse(file, "fasta"):
    if GCcont < GC(record.seq):
        GCcont = GC(record.seq)
        GCname = record.id

print GCname
print round(GCcont,2), "%"