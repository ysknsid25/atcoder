n=int(input())
a=[0]+list(map(int,input().split()))

k=0
for i in range(1,n+1):
  if i==a[i]:
    k+=1

#! kC2より
ans = k*(k-1)//2

for i in range(1,n+1):
  j=a[i]
  if i<j and a[j]==i:
    ans+=1

print(ans)