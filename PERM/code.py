import numpy as np
import math

def permutations(arr, position, end):
    if position == end:
        print(' '.join(str(i) for i in arr))

    else:
        for index in range(position, end):

            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]



with open('rosalind_perm.txt', 'r') as f:
    n = int(f.readlines()[0].rstrip('\n'))

    print(math.factorial(n))

    permutations([i+1 for i in range(n)], 0, n)