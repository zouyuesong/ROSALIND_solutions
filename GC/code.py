import numpy as np 

def get_GC_content(DNA):
    # print(DNA, DNA.count('C') + DNA.count('G'))
    return (DNA.count('C') + DNA.count('G')) / len(DNA) * 100


with open('rosalind_gc.txt', 'r') as f:
    lines = f.readlines()
    names = []
    GC_contents = []
    DNA = ''
    for (i, line) in enumerate(lines):
        if line[0] == '>': 
            names.append(line.strip().lstrip('>'))
            DNA = ''
            for j in range(i + 1, len(lines)): 
                if lines[j][0] == '>':
                    break
                DNA += lines[j].strip()
            GC_contents.append(get_GC_content(DNA))
    GC_contents = np.array(GC_contents)
    id = np.argmax(GC_contents)
    print(names[id])
    print(GC_contents[id])
