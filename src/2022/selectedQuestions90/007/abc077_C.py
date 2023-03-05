import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

cnt = 0
lenc = len(c)

for i in b:
    tmpa = bisect.bisect_left(a, i)
    tmpc = bisect.bisect_right(c, i)
    numa = tmpa
    numc = lenc - tmpc
    num = numa * numc
    cnt += num

print(cnt)
