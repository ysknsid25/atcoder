n,w=map(int,input().split())
cheese=[0]*n
for i in range(n):
    cheese[i]=list(map(int,input().split()))
cheese.sort(reverse=True)
ans=0
now=0
for a,b in cheese:
    remain=w-now
    if remain==0:
        break
    if remain>=b:
        now+=b
        ans+=b*a
    else:
        now+=remain
        ans+=remain*a
print(ans)