n=int(input())
ans=0
for num in range(1,n+1,2):
  a=1
  cnt=0
  while a*a<=num:
    if num%a==0:
      b=num//a
      if a==b:
        cnt+=1
      else:
        cnt+=2
    a+=1
  if cnt==8:
    ans+=1
print(ans)