from itertools import groupby


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


start = input().split()
goal = input().split()

startrunlen = runLengthEncode(start[0])
goalrunlen = runLengthEncode(goal[0])

if len(startrunlen) != len(goalrunlen):
    print("No")
    exit()

out = "Yes"
for i in range(0, len(startrunlen)):
    stuple = startrunlen[i]
    gtuple = goalrunlen[i]
    if stuple[0] != gtuple[0]:
        out = "No"
        break
    elif stuple[1] > gtuple[1]:
        out = "No"
        break
    elif stuple[1] == 1 and stuple[1] < gtuple[1]:
        out = "No"
        break

print(out)
