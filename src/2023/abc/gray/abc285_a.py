a,b=map(int,input().split())
a2=2*a
a21=2*a+1
b2=2*b
b21=2*b+1

if a2==b or a21==b:
    print("Yes")
elif b2==a or b21==a:
    print("Yes")
else:
    print("No")