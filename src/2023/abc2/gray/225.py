n,m=map(int, input().split())
memo=[0]*m
for i in range(n):
    b=list(map(int, input().split()))
    for j in range(m):
        mod=(b[j]-1)%7
        if i==0:
            memo[j]=mod
            if j==0 and b[0]+7 < b[m-1]:
                print('No')
                exit()
            if j>0 and memo[j-1]+1!=memo[j] and memo[j-1]<7 and memo[j]<7:
                print('No')
                exit()
        else:
            if mod!=memo[j]:
                print('No')
                exit()
print('Yes')
