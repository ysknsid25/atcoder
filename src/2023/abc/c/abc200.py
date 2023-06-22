n=int(input())
a=list(map(int,input().split()))
s=[0 for i in range(200)]
for i in range(n):
    s[a[i]%200]+=1

ans=0
for mod in range(200):
    ans+=s[mod]*(s[mod]-1)//2

print(ans)