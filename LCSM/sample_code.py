def substr_in_all(arr, part):
  for dna in arr:
    if dna.find(part)==-1:
      return False
  return True

def common_substr(arr, l):
  first = arr[0]
  for i in range(len(first)-l+1):
    part = first[i:i+l]
    if substr_in_all(arr, part):
      return part
  return ""

def longest_common_substr(arr):
  import time
  sta = time.time()

  l = 0; r = len(arr[0])

  while l+1<r:
    mid = int((l+r) / 2)
    if common_substr(arr, mid)!="":
      l=mid
    else:
      r = mid
  end = time.time()
  print('Time: ' + str(end - sta) + 's')

  return common_substr(arr, l)


DNAs = []

with open('rosalind_lcsm.txt', 'r') as f:
    buf = f.readline().strip()
    while buf:
        name = buf[1:]
        DNA = ''
        buf = f.readline().strip()
        while buf and not buf.startswith('>'): 
            DNA += buf
            buf = f.readline().strip()
        DNAs.append(DNA)
print(longest_common_substr(DNAs))
