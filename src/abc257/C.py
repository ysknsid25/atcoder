n = int(input())
s = input()
w = list(map(int, input().split()))

sarr = list(s)
wmap = {}
for i in range(n):
    wi = w[i]
    if wi in wmap:
        tmp = list(wmap[wi])
        tmp.append(i)
        wmap[wi] = tmp
    else:
        wmap[wi] = [i]

sortedwmap = sorted(wmap.items())

now = 0
for judge in sarr:
    if judge == "1":
        now += 1

max = now
ans = now
for judgetuple in sortedwmap:
    whoarr = judgetuple[1]
    for who in whoarr:
        if s[who] == "1":
            ans -= 1
        else:
            ans += 1
    if ans > max:
        max = ans

print(max)
