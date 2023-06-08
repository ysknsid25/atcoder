a,b,c=map(int,input().split())
d=a//c
e=b//c
for x in range(d,e+1):
    if a<=x*c<=b:
        print(x*c)
        exit()
print(-1)
