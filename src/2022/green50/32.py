n = int(input())
i = 1
ans = 0

nn = 2 * n
while i * i <= nn:
  if nn % i == 0:
    x = i
    y = nn // i
    if x % 2 != y % 2:
      ans += 2
  i += 1

print(ans)