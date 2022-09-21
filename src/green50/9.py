n = int(input())

sevenmap = {}
for i in range(1,n+1):
  strnum = str(i)
  if strnum.find("7") > -1:
    sevenmap[strnum] = 1
    continue
  stroct = '{:o}'.format(i)
  if stroct.find("7") > -1:
    sevenmap[strnum] = 1
    continue

sevencnt = len(sevenmap)
ans = n - sevencnt
print(ans)