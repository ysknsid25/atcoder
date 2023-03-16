x,k,d = map(int,input().split())

x=abs(x)
div=x//d

if div <= k:
    k-=div
    y=x%d
    if k%2 == 0:
        print(y)
    else:
        print(abs(y-d))
else:
    print(abs(x-(d*k)))