from collections import deque

s=input()
q=int(input())

que=deque()
for i in range(len(s)):
    que.append(s[i])

isReverse = False
for i in range(q):
    tmp=list(map(str, input().split()))
    qr=tmp[0]
    if qr == "1":
        isReverse = not isReverse
    else:
        f=tmp[1]
        if isReverse:
            if f=="1":
                que.append(tmp[2])
            else:
                que.appendleft(tmp[2])
        else:
            if f=="1":
                que.appendleft(tmp[2])
            else:
                que.append(tmp[2])

que=list(que)
if isReverse:
    que.reverse()

print("".join(que))