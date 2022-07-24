def getInputFile():
    f = open('M:\\project\\atcoder\\src\\sample.txt', 'r')
    datalist = f.readlines()
    f.close()
    return datalist


def removeReturncd(str):
    return str.rstrip('\n')


inputs = getInputFile()

# ここから入れ替える
n = int(inputs[0])

adanaseiarr = []
adanameiarr = []
result = "Yes"
for i in range(n):
    s, t = inputs[i+1].split()
    adanaseiarr.append(s.rstrip('\n'))
    adanameiarr.append(t.rstrip('\n'))

for i in range(n):
    sei = adanaseiarr[i]
    mei = adanameiarr[i]
    isExistSei = False
    isExistMei = False
    for j in range(n):
        if i == j:
            continue
        isExistSei = isExistSei or sei == adanaseiarr[j] or sei == adanameiarr[j]
        isExistMei = isExistMei or mei == adanameiarr[j] or mei == adanaseiarr[j]
    if isExistSei and isExistMei:
        print("No")
        exit()

print("Yes")
