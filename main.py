def getInputFile():
    f = open('M:\\project\\atcoder\\src\\sample.txt', 'r')
    datalist = f.readlines()
    f.close()
    return datalist


def removeReturncd(str):
    return str.rstrip('\n')


inputs = getInputFile()

# ここから入れ替える


n, q = map(int, inputs[0].split())
s = inputs[1]

t = 0
for i in range(2, len(inputs)):
    query = inputs[i].split()
    direct = query[0]
    posi = int(query[1])
    if direct == '1':
        nowposi = nextbeginposi(posi, n)
    else:
        outposi = nextbeginposi((nowposi+posi), n)
        print(s[outposi-1:outposi])
