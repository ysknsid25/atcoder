n, k  = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = [0] * n

for i in range(0, n):
  ta = a[i]
  tb = b[i]
  td = abs(ta - tb)
  d[i] = td

dsum = sum(d)

if dsum > k:
  print("No")
elif dsum == k:
  print("Yes")
else:
  diff = k - dsum
  if diff%2 == 0:
    print("Yes")
  else:
    print("No")
