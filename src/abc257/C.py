n = int(input())
s = int(input())
w = list(map(int, input().split()))

wmap = {}
sortedw = w.sort()
for i in range(n):
    wi = w[i]
    tmpArr = []
    if wi in wmap:
        tmpArr = wmap[wi]
    tmpArr.append(wi)
    wmap[wi] = tmpArr

sarr = list(s)
now = 0
for i in range(len(s)):
    if sarr[i] == "1":
        now += 1

ans = now
