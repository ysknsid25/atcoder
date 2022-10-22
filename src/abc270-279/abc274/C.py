import math

n = int(input())
a = list(map(int, input().split()))

ameba = set()
for i in range(n):
  num = a[i]
  ameba.add(num)
  num *= 2
  ameba.add(num)
  num += 1
  ameba.add(num)

for num in ameba:
  if num == 1:
    print(0)
    continue

  if num % 2 == 1:
    num = num - 1
  gen = math.log2(num)
  print(int(gen))