n = int(input())

total = 1
for i in range(n):
  a = list(map(int, input().split()))
  total *= sum(a)

ans = total % 1000000007
print(ans)