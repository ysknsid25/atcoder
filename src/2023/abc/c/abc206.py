n=int(input())
a=list(map(int,input().split()))
cntmap={}
for num in a:
    if num in cntmap:
        cntmap[num]+=1
    else:
        cntmap[num]=1

ans=0
now=n
for num in a:
    cnt=cntmap[num]
    ans+=now-cnt
    now-=1
    cntmap[num]-=1
print(ans)