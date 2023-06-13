n,x=map(int,input().split())
a=list(map(int,input().split()))
suma=sum(a)
wari=n//2
if suma-wari<=x:
    print("Yes")
else:
    print("No")