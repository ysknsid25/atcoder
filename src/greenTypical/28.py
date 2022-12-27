n,x=map(int,input().split())
res=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  l=tmp[0]
  tmp_res=[]
  for j in range(1,l+1):
    num=tmp[j]
    if i==0:
      tmp_res.append(num)
    else:
      for y in res:
        calc=num*y
        if calc>x:
          continue
        else:
          tmp_res.append(calc)
  res=tmp_res
  
ans=0
for num in res:
  if num==x:
    ans+=1
print(ans)