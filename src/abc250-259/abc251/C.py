n = int(input())

smap = {}
simap = {}
iarr = []
for i in range(0, n):
    s, t = input().split()
    if not s in smap:
        smap[s] = int(t)
        simapkey = str(s) + str(t)
        simap[simapkey] = i

max_k = max(smap, key=smap.get)

maxikey = str(max_k) + str(smap[max_k])
maxindex = simap[maxikey] + 1
print(maxindex)
