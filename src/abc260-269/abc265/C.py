# 移動後のi, jのいずれかが0未満もしくはH, W超過になれば移動終了
# もしくは一度通ったマスの位置にきた場合は、無限に移動するので-1を出力

h, w = map(int, input().split())

dirarr =[[""] * w] * h 
acarr = [[False] * w for i in range(h)]

for i in range(0, h):
  tmp = list(input())
  dirarr[i]= tmp

isInfiniti = False
goalh = 1
goalw = 1
i = 1
j = 1

while(True):
    iindex = i -1
    jindex = j -1
    if acarr[iindex][jindex]:
      isInfiniti = True
      break

    acarr[iindex][jindex] = True
    direct = dirarr[iindex][jindex]
    goalh = i
    goalw = j
    if direct == "U":
      i -= 1
    elif direct == "D":
      i += 1
    elif direct == "L":
      j -= 1
    elif direct == "R":
      j += 1
    #print(str(i) + "@" + str(j))
    if i <= 0 or j <= 0 or i > h or j > w:
      break

if isInfiniti:
  print(-1)
else:
  print(str(goalh) + " " + str(goalw))