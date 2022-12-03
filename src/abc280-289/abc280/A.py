h,w = map(int,input().split())
ans = 0
for i in range(h):
  s = list(input())
  for c in s:
    if c == "#":
      ans += 1
print(ans)