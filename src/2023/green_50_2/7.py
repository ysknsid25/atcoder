h,w,x,y = map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))

ans=1
x-=1
y-=1
#右
for i in range(y+1,w):
    if s[x][i]==".":
        ans+=1
    else:
        break
#左
for i in range(y-1,-1,-1):
    if s[x][i]==".":
        ans+=1
    else:
        break
#下
for i in range(x+1,h):
    if s[i][y]==".":
        ans+=1
    else:
        break
#上
for i in range(x-1,-1,-1):
    if s[i][y]==".":
        ans+=1
    else:
        break
print(ans)