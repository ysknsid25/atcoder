n=int(input())
a=list(map(int,input().split()))
memo=[False for i in range(n+1)]

for num in a:
    if memo[num]:
        print("No")
        exit()
    else:
        memo[num]=True
print("Yes")