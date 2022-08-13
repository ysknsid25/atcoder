intlist = list(map(int, input().split()))
cnt = 0
nextIndex = 0
while(True):
    if cnt == 2:
        break
    nextIndex = intlist[nextIndex]
    cnt += 1
print(intlist[nextIndex])
