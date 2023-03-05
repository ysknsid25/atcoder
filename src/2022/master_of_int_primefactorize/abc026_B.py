n=int(input())
i=1
res=set()
while i*i<=n:
  if n%i==0:
    res.add(i)
    res.add(n//i)
  i+=1
res=list(res)
comp=sum(res)-n
if comp == n:
  print("Perfect")
elif comp < n:
  print("Deficient")
else:
  print("Abundant")