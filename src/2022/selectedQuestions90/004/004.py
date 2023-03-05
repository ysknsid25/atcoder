h, w = map(int, input().split())

arr = []
for i in range(0, h):
  arr.append(list(map(int, input().split())))

rowsum = []
colsum = []
for i in range(0, h):
  rowsum.append(sum(arr[i]))
  
for i in range(0, w):
  tmpsum = 0
  for j in range(0, h):
    tmpsum += arr[j][i]
  colsum.append(tmpsum)
  
for i in range(0, h):
  out = ""
  for j in range(0, w):
    tmpsum = rowsum[i] + colsum[j] - arr[i][j]
    out = out + str(tmpsum)
    if j != (w-1):
      out = out + " "
  print(out)
    