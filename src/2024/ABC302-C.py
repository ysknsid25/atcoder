from collections import defaultdict

n,m = map(int, input().split())
strs = sorted([list(input()) for i in range(n)])

for i in range(0, n-1):
  a = strs[i]
  b = strs[i+1]
  a_dict = defaultdict(int)
  b_dict = defaultdict(int)
  appears = set()
  for char_a in a:
    appears.add(char_a)
    a_dict[char_a] += 1
  for char_b in b:
    appears.add(char_a)
    b_dict[char_b] += 1
  
  a_diff = 0
  b_diff = 0
  for char in appears:
    a_char = a_dict[char]
    b_char = b_dict[char]
    a_diff += abs(a_char - b_char)
    b_diff += abs(b_char - a_char)

  if a_diff > 2 or b_diff > 2:
    print('No')
    exit()

print('Yes')