n = int(input())

i=1
ans = []
while i**2 <= n:
  if n%i==0:
    ans.append(i)
    if i != n/i:
      ans.append(n//i)
  i+=1

ans.sort()
for j in ans:
  print(j)