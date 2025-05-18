n=int(input())
d={}
def chk(x):
    if(x in d):
        return d[x]+x
    elif(x==1):
        return 0
    else:
        up=x//2
        down=(x+1)//2
        ans=chk(up)+chk(down)
        d[x]=ans
        return ans+x
ans=chk(n)
print(ans)
