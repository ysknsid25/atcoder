a,b,c,d=map(int,input().split())
blue=a
red=0
for i in range(10**5+1):
    if blue<=red*d:
        print(i)
        exit()
    blue+=b
    red+=c
print(-1)