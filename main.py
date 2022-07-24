def getInputFile():
    f = open('M:\\project\\atcoder\\src\\sample.txt', 'r')
    datalist = f.readlines()
    f.close()
    return datalist


def removeReturncd(str):
    return str.rstrip('\n')


inputs = getInputFile()

# ここから入れ替える
s = inputs[0]
arr = list(s.rstrip('\n'))

result = "0"
for i in range(1, len(arr)):
    if arr[i-1] == "1":
        result = result + "1"
    else:
        result = result + "0"

print(result)
