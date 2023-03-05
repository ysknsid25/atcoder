n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = 0
for i in range(0, n):
  dist = abs((a[i] - b[i]))
  ans += dist

print(ans)