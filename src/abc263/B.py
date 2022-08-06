n = int(input())
p = list(map(int, input().split()))

notfound = True
nowc = n - 2
gen = 0
while(notfound):
    beforep = p[nowc]
    if beforep == 1:
        gen += 1
        break
    else:
        nowc = beforep - 2
        gen += 1

print(gen)
