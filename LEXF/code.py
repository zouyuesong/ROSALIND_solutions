import numpy as np
import math

def enumeration(arr, n, cur, l, symbol):
    if cur == l:
        print(''.join(symbol[i] for i in arr))

    else:
        for index in range(n):
            arr.append(index)
            enumeration(arr, n, cur+1, l, symbol)
            arr.pop()



with open('rosalind_lexf.txt', 'r') as f:
    symbol = f.readline().strip().split(' ')
    n = len(symbol)
    l = int(f.readline().rstrip('\n'))

    # print(symbol)
    # print(n**l)

    enumeration([], n, 0, l, symbol)