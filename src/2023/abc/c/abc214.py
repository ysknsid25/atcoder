n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))

df=10**9
ans=[df for i in range(n)]

# 普通にもらったとき
for i in range(n):
    before = i-1
    if before < 0:
        before = n-1
    ans[i] = min(ans[before]+s[before],t[i])

# i-1番めの人がもらう時間が極端に遅い時(t[i-1] > sum(t) - t[i-1])
for i in range(n):
    before = i-1
    if before < 0:
        before = n-1
    ans[i] = min(ans[before]+s[before],ans[i])

for i in range(n):
    print(ans[i])