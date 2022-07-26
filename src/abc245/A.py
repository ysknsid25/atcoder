def paddingzero(strnum):
    intnum = int(strnum)
    if intnum < 10:
        return "0" + str(intnum)
    return str(intnum)


A, B, C, D = input().split()

takahashi = paddingzero(A) + paddingzero(B) + "0"
aoki = paddingzero(C) + paddingzero(D) + "1"

if int(takahashi) < int(aoki):
    print("Takahashi")
else:
    print("Aoki")
