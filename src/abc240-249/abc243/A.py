v, a, b, c = map(int, input().split())

people = [a, b, c]
who = {0: "F", 1: "M", 2: "T"}

remain = v
cnt = 0
while(True):
    i = cnt % 3
    remain = remain - people[i]
    if(remain < 0):
        print(who[i])
    cnt += 1
