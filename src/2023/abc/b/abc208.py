p=int(input())
ans=0
nxt=p
n=10*9*8*7*6*5*4*3*2
for i in range(10,0,-1):
    tmp=nxt//n
    if tmp>100:
        tmp=100
        nxt-=100*n
    else:
        nxt=nxt%n
    ans+=tmp
    n=n//i
print(ans)