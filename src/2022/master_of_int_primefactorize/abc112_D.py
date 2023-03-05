n,m=map(int,input().split())
res=[]
a=1
while a*a<=m:
    if m%a==0:
      res.append(a)
      b=m//a
      if a!=b:
        res.append(b)
    a+=1

ans=-1
for num in res:
  if m-(n*num) >=0:
    ans=max(ans,num)
print(ans)