n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
ans=[10**9+7]*n

for i in range(n):
    before=i-1
    if i==0:
        before=n-1
    ans[i]=min(t[i],ans[before]+s[before])

for i in range(n):
    before=i-1
    if i==0:
        before=n-1
    ans[i]=min(ans[i],ans[before]+s[before])
    print(ans[i])