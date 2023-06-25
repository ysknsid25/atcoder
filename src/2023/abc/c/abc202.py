n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
bc=[]
for j in c:
    bc.append(b[j-1])

acount=[0 for i in range(n+1)]
for i in range(n):
    acount[a[i]]+=1

bccount=[0 for i in range(n+1)]
for i in range(n):
    bccount[bc[i]]+=1

ans=0
for i in range(n+1):
    ans+=acount[i]*bccount[i]
print(ans)