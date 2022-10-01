n = int(input())
x = '{:X}'.format(n)
if len(x) == 1:
  x = "0" + x
print(x)