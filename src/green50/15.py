n = input()
nlist = list(n)

mods = []
modzero = 0
modone = 0
modtwo = 0
for i in range(len(nlist)):
  intn = int(nlist[i])
  mod = intn % 3
  if mod == 0:
    modzero += 1
  elif mod == 1:
    modone += 1
  else:
    modtwo += 1
  mods.append(mod)

total = sum(mods)
totalmod = total % 3
intn = int(n)

if totalmod == 0:
  print(0)
elif totalmod == 1:
  if modone > 0 and intn > 9:
    print(1)
  elif modone > 0 and intn <= 9:
    print(-1)
  elif modone == 0 and intn > 99:
    print(2)
  else:
    print(-1)
else:
  if modtwo > 0 and intn > 9:
    print(1)
  elif modtwo > 0 and intn <= 9:
    print(-1)
  elif modtwo == 0 and intn > 99:
    print(2)
  else:
    print(-1)