import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

cnt = 0
for i in a:
  numb = bisect.bisect_right(b, i)
  rangeb = 0
  if numb != 0:
    rangeb = numb
  for j in range(rangeb, n):
      valb = b[j]
      numc = bisect.bisect_right(c, valb)
      tmp = n - numc
      cnt += tmp

print(cnt)