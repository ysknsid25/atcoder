n = input()
intn = int(n)
listn = list(n)

zerocnt = 0
onecnt = 0
twocnt = 0
for strnum in listn:
  num = int(strnum)
  mod = num%3
  if mod == 0:
    zerocnt += 1
  elif mod == 1:
    onecnt += 1
  else:
    twocnt += 1

mod = intn % 3

if mod == 0:
  print(0)
elif mod == 1:
  if onecnt >= 1:
    if len(n) <= 1:
      print(-1)
    else:
      print(1)
  else:
    if len(n) <= 2:
      print(-1)
    else:
      print(2)
else:
  if twocnt >= 1:
    if len(n) <= 1:
      print(-1)
    else:
      print(1)
  else:
    if len(n) <= 2:
      print(-1)
    else:
      print(2)
