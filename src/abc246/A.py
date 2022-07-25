xmap = {}
ymap = {}

for i in range(3):
    x, y = map(int, input().split())
    if x in xmap:
        xmap[x] = xmap[x] + 1
    else:
        xmap[x] = 1
    if y in ymap:
        ymap[y] = ymap[y] + 1
    else:
        ymap[y] = 1
        
x = 1000
for k in xmap:
    if xmap[k] % 2 == 1:
        x = k
        break

y = 1000
for k in ymap:
    if ymap[k] % 2 == 1:
        y = k
        break


print(str(x) + " " + str(y))
