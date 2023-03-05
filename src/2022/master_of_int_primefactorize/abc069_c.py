n=int(input())
a=list(map(int,input().split()))
border=n//2
cnt=0
cnt2=0
for i in range(n):
    num=a[i]
    j=0
    haveFour=False
    while num%2==0:
      num/=2
      j+=1
      if j>=2:
        haveFour=True
        break
    if j==1:
      cnt2+=1
    if haveFour:
      cnt+=1

if cnt2>1:
  cnt2//=2
else:
  cnt2=0

if (cnt+cnt2)>=border:
  print("Yes")
else:
  print("No")