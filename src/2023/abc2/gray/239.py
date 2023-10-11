x1,y1,x2,y2 = map(int,input().split())
dist=[
    [-2,1],
    [-1,2],
    [2,1],
    [1,2],
    [-2,-1],
    [-1,-2],
    [1,-2],
    [2,-1],
]

for x,y in dist:
    x3=x1+x
    y3=y1+y
    d=(x3-x2)**2+(y3-y2)**2
    if d==5:
        print("Yes")
        exit()

print("No")