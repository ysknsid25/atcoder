cards = list(map(int, input().split()))

cardmap = {}
for card in cards:
    if card in cardmap:
        cnt = cardmap[card]
        cnt += 1
        cardmap[card] = cnt
    else:
        cardmap[card] = 1
if len(cardmap) == 2:
    for val in cardmap.values():
        if (val == 2 or val == 3):
            print("Yes")
            exit()

print("No")
