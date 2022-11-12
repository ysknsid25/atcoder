n = int(input())
smap = {}
isSatisfy = True
for i in range(n):
  s = input()
  if s in smap:
    isSatisfy = False
    break
  else:
    smap[s] = s
    slist = list(s)
    s1 = slist[0]
    s2 = slist[1]
    if s1 == "H" or s1 == "D" or s1 == "C" or s1 == "S":
      if s2 == "A" or s2 == "2" or s2 == "3" or s2 == "4" or s2 == "5" or s2 == "6" or s2 == "7" or s2 == "8" or s2 == "9" or s2 == "T" or s2 == "J" or s2 == "Q" or s2 == "K":
        continue
      else:
        isSatisfy = False
        break   
    else:
      isSatisfy = False
      break

if isSatisfy:
  print("Yes")
else:
  print("No")