n = int(input())
a = list(map(int, input().split()))
total = sum(a)

ans = 0
nextTotal = total
for i in range(0, n):
  tmptotal = nextTotal - a[i]
  ans += tmptotal * a[i]
  nextTotal = tmptotal

mod = 10 ** 9 + 7
ans = ans % mod

print(ans)