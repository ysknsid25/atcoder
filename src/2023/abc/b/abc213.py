n=int(input())
a=list(map(int,input().split()))
minn=-10**9
minn2=-10**9
minni=0
minni2=0
for i in range(n):
    num=a[i]
    if num>=minn:
        minn2=minn
        minni2=minni
        minn=num
        minni=i+1
    elif num>=minn2:
        minn2=num
        minni2=i+1
print(minni2)