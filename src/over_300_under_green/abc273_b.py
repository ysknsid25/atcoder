x,k=map(str,input().split())

k=int(k)
n=len(x)

if n<k:
    print(0)
    exit()

x=list(x)
for i in range(n):
    x[i]=int(x[i])

x=[0]+x
for i in range(n, n-k, -1):
    if 5<=x[i]:
        x[i-1]+=1
    x[i]=0

for i in range(n, 0, -1):
    if 10<=x[i]:
        x[i-1]+=1
        x[i]-=10

ans=""
for i in range(n+1):
    ans+=str(x[i])

ans=int(ans)
print(ans)