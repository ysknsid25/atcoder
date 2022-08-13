a = int(input())
rangeint = 2 ** 31
minusrangeint = rangeint * -1

if a >= minusrangeint and a < rangeint:
  print("Yes")
else:
  print("No")