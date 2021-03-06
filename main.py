def getInputFile():
    f = open('M:\\project\\atcoder\\src\\sample.txt', 'r')
    datalist = f.readlines()
    f.close()
    return datalist


def removeReturncd(str):
    return str.rstrip('\n')


inputs = getInputFile()

# ここから入れ替える


def getNextDist(nowdist):
    nextdist = nowdist + 1
    if nextdist > 4:
        return 1
    return nextdist


n = int(inputs[0])
t = inputs[1].split()
tarr = list(t[0])

distmap = {1: 1, 2: -1, 3: -1, 4: 1}

nowdist = 1
x = 0
y = 0
for i in range(n):
    direct = tarr[i]
    if direct == "S":
        if nowdist == 1 or nowdist == 3:
            x = x + distmap[nowdist]
        if nowdist == 2 or nowdist == 4:
            y = y + distmap[nowdist]
    else:
        nowdist = getNextDist(nowdist)

print(str(x) + " " + str(y))
