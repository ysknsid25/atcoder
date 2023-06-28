n=int(input())
ranges=[]
for i in range(n):
    t,l,r=map(int,input().split())
    if t==2:
        r-=0.1
    elif t==3:
        l+=0.1
    elif t==4:
        l+=0.1
        r-=0.1
    ranges.append([l,r])

ans=0
for i in range(n):
    for j in range(i+1,n):
        la=ranges[i][0]
        ra=ranges[i][1]
        lb=ranges[j][0]
        rb=ranges[j][1]
        if la<=lb and lb<=ra:
            ans+=1
        elif la<=rb and rb<=ra:
            ans+=1
        elif lb<=la and la<=rb:
            ans+=1
        elif lb<=ra and ra<=rb:
            ans+=1
print(ans)