from collections import defaultdict, deque

h,w=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(h)]

dic=defaultdict(int)
q=deque()
q.append((0,0, dic))

ans=0
while q:
    x,y,dic=q.popleft()
    if x==h-1 and y==w-1:
        if a[x][y] not in dic:
            ans+=1
    else:
        if a[x][y] not in dic:
            dic2=dic.copy()
            dic2[a[x][y]]+=1
            rx, ry = x, y+1
            ux, uy = x+1, y
            if 0 <= ry < w:
                q.append((rx, ry, dic2))
            if 0 <= ux < h:
                q.append((ux, uy, dic2))

print(ans)
