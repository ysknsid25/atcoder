def getInputFile():
    f = open('/Users/yoshidakengo/project/atcoder/src/sample.txt', 'r')
    datalist = f.readlines()
    f.close()
    return datalist


def removeReturncd(str):
    return str.rstrip('\n')


inputs = getInputFile()

# ここから入れ替える

print(inputs)
