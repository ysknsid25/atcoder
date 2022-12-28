n=int(input())
ans=0
a=1
#! a*a*a<=nが最小となる
while a**3<=n:
  b=a
  #! aが決まったら、最小でもb=cと考えると、b*b<=√n/aより
  while a*b**2<=n:
    #! cの個数はb<=c<=n/abの切り捨て ただしb=cの場合+1することになる
    ans+=int(n/(a*b))-b+1
    b+=1
  a+=1
print(ans)