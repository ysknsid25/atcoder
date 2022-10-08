n = int(input())
a = list(map(int, input().split()))

even = []
odd = []
for i in range(n):
  num = a[i]
  if num % 2 == 0:
    even.append(num)
  else:
    odd.append(num)

if len(even) < 2 and len(odd) < 2:
  print(-1)
else:
  evenmax = 0
  oddmax = 0
  even.sort(reverse=True)
  odd.sort(reverse=True)
  if len(even) > 1:
    evenmax = even[0] + even[1]
  if len(odd) > 1:
    oddmax = odd[0] + odd[1]
  print(max(evenmax, oddmax))