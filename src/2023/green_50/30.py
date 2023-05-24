x=int(input())
for a in range(-1000,1001, 1):
    for b in range(-1000,1001, 1):
        res=a**5-b**5
        if res==x:
            print(a,b)
            exit()