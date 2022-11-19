n=int(input())
ans=[]
i=1
while i*i <= n:
  if n%i==0:
    ans.append(i)
    res = n//i
    if i!=res:
      ans.append(res)
  i+=1
ans.sort()
for num in ans:
  print(num)