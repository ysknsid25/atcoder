n = int(input())
s = [list(input()) for _ in range(n)]

appearmap = {}
for i in range(0, 10):
    search = str(i)
    indexarr = []
    for arr in s:
        index = arr.index(search)
        indexarr.append(index)
    appearmap[search] = indexarr

mintime = 10000000000000000000
minnumber = -1

for k, v in appearmap.items():
    timesmap = {}
    for t in v:
        if t in timesmap:
            timesmap[t] = timesmap[t] + 1
        else:
            timesmap[t] = 1
    maxtime = -1
    for tk, tv in timesmap.items():
        tmp = tk + (10 * (tv - 1))
        if maxtime < tmp:
            maxtime = tmp

    if mintime > maxtime:
        mintime = maxtime
        minnumber = k

print(mintime)
