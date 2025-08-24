x,y=map(int, input().split())
mod=(x+y)%12
if mod==0:
    print(12)
else:
    print(mod)
