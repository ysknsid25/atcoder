n=int(input())

ans = set()
num=1
while num*num <= n:
  if n%num == 0:
    ans.add(num)
    ans.add(n//num)
  num += 1

ans=list(ans)
ans.sort()
for num in ans:
  print(num)