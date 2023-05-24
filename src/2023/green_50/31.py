n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=list(input())

te=[]

now=0
ans=0
for aite in t:
    myte="@"
    kakote = "@"
    if now-k >= 0:
      kakote = te[now-k]
    if aite == 'r':
      if kakote != 'p':
        ans+=p
        myte='p'
    elif aite == 's':
      if kakote != 'r':
        myte='r'
        ans+=r
    else:
      if kakote != 's':
        myte='s'
        ans+=s
    te.append(myte)
    now+=1
print(ans)
