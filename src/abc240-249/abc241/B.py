n, m = map(int, input().split())
pastalist = list(map(int, input().split()))
eatplanlist = list(map(int, input().split()))

cando = "Yes"

for i in range(0, m):
    wantPasta = eatplanlist[i]
    isExist = wantPasta in pastalist
    if isExist:
        index = pastalist.index(wantPasta)
        pastalist.pop(index)
    else:
        cando = "No"
        break

print(cando)
