h,w=map(int,input().split())
g=[[] for i in range(h+1)]
for i in range(h):
    g[i+1]=[""]+list(input())

memo={}
i=1
j=1
while True:
    stri=str(i)
    strj=str(j)
    key=stri+"@"+strj
    if key in memo:
        print(-1)
        exit()
    else:
        memo[key]=1

    nxti=i
    nxtj=j
    now=g[i][j]
    if now=='L':
        nxtj-=1
    elif now=='R':
        nxtj+=1
    elif now=='U':
        nxti-=1
    else:
        nxti+=1
    if nxti<=0 or nxti>h or nxtj<=0 or nxtj>w:
        print(i,j)
        exit()

    i=nxti
    j=nxtj
