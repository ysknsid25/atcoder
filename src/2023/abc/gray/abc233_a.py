x,y=map(int,input().split())
a=y-x
if a<0:
    print(0)
    exit()
b=a//10
mod=a%10
ans=b
if mod!=0:
    ans+=1
print(ans)