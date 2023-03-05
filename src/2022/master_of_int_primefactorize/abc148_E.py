n=int(input())
if n%2==1:
  print(0)
  exit()

n2=n//2
ans=0
while n2>1:
  ans+=n2//5
  n2//=5
print(ans)