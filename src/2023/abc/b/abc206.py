n=int(input())
for i in range(1, 10**6+1):
    res=i*(i+1)//2
    if res>=n:
        print(i)
        exit()