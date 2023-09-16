n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

d=[0]*(n+1)
for x in c:
    d[b[x-1]]+=1

ans=0
for x in a:
    ans+=d[x]
print(ans)