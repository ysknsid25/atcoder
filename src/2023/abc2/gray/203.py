n,k=map(int,input().split())
friends=[[] for i in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    friends[i]=[a,b]
friends.sort()
now=k
for i in range(n):
    v=friends[i][0]
    if v<=now:
        now+=friends[i][1]
    else:
        break
print(now)