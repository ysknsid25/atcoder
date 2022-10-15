x, k = map(int, input().split())
xstr = str(x)
xlist = list(xstr)
degit = len(xlist)
xlist.reverse()

if degit <= k:
  print(0)
  exit()

for i in range(k):
  if degit - 1 < i:
    break
  n = int(xlist[i])
  if n > 4:
    nx = i + 1
    if degit - 1 < nx:
      xlist.append("1")
    else:
      nxnum = int(xlist[nx])
      nxnum += 1
      xlist[nx] = str(nxnum)
  xlist[i] = "0"

xlist.reverse()
ans = "".join(xlist)
ans = int(ans)
print(ans)