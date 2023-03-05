n=int(input())
a=list(map(int,input().split()))
k=int(input())

a_sum=sum(a)
cnt=k//a_sum
mod=k%a_sum

ans=cnt*n
tmp=0
for i in range(n):
  ans+=1
  tmp+=a[i]
  if tmp > mod:
    break

print(ans)