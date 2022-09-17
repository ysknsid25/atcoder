n = int(input())
binn = format(n, 'b')

for i in range(n+1):
  bin2 = format(i, 'b')
  binand = binn & bin2
  if bin2 == binand:
    print(i)
    