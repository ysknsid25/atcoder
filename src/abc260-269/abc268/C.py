n = int(input())
p = list(map(int, input().split()))

cnt = [0 for i in range(n)]
for i in range(n):
  j = (p[i]-i-1) % n
  for k in range(0,3):
    cnt[(j+k)%n] += 1

ans = 0
for i in range(n):
  ans = max(ans, cnt[i])

print(ans)