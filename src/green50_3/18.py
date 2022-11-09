n = int(input())
a = list(map(int, input().split()))
suma = sum(a)

ans = 0
for num in range(1, n+1):
  index = num-1
  suma -= a[index]
  ans += suma * a[index]

ans %= 10**9+7
print(ans)