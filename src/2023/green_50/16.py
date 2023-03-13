import itertools
n,k=map(int,input().split())
t=[[]]
for i in range(n):
    time=[0] + list(map(int,input().split()))
    t.append(time)

ans=0
nums=[x for x in range(2,n+1)]
p = itertools.permutations(nums, n-1)
for c in p:
    total = 0
    fr=1
    for to in c:
        time=t[fr][to]
        total += time
        fr=to
    time=t[fr][1]
    total += time
    if total == k:
        ans+=1

print(ans)