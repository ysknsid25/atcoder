n=int(input())
ran=[]
for n in range(n):
    t,l,r=map(int,input().split())
    if t==1:
        ran.append([l,r])
    else:
        if t==2:
            ran.append([l,r-0.1])
        elif t==3:
            ran.append([l+0.1,r])
        else:
            ran.append([l+0.1,r-0.1])
ans=0
for i in range(n):
    for j in range(i+1,n+1):
        al,ar=ran[i]
        bl,br=ran[j]
        if ar<bl or br<al:
            continue
        ans+=1
print(ans)