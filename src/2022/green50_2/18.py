n = int(input())
a = list(map(int, input().split()))

total = sum(a)
tmptotal = total
ans = 0
for i in range(n):
  num = a[i]
  tmptotal -= num
  ans += (num * tmptotal)

ans %= (10 ** 9 + 7)
print(ans)