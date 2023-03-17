n=int(input())
s=list(input())
q=int(input())

isReverse = False
for i in range(q):
    t,a,b=map(int,input().split())
    a-=1
    b-=1
    if t == 1:
        if isReverse:
            a=(a+n)%(2*n)
            b=(b+n)%(2*n)
        x=s[a]
        y=s[b]
        s[a]=y
        s[b]=x
    else:
        isReverse= not isReverse

if isReverse:
    s=s[n:] + s[0:n]
print("".join(s))