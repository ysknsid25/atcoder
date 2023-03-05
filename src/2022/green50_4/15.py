org = int(input())
n=list(str(org))
modorg = org%3
mod0 = 0
mod1 = 0
mod2 = 0
d = len(n)
for strn in n:
  intn = int(strn)
  mod = intn % 3
  if mod==0:
    mod0 += 1
  elif mod==1:
    mod1 += 1
  else:
    mod2 += 1

if modorg == 0:
  print(0)
elif modorg ==1:
  if mod1 >= 1:
    if d > 1:
      print(1)
    else:
      print(-1)
  elif mod2 >= 2:
    if d > 2:
      print(2)
    else:
      print(-1)
elif modorg ==2:
  if mod2 >= 1:
    if d > 1:
      print(1)
    else:
      print(-1)
  elif mod1 >= 2:
    if d > 2:
      print(2)
    else:
      print(-1)