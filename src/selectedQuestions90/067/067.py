def Base_10_to_n(n, b):
    if n // b:
        return Base_10_to_n(n // b, b) + str(n % b)
    return str(n % b)

n, k = map(str, input().split())

if n == '0':
  print(n)
  exit()

num = int(n)
for i in range(0, int(k)):
  tmp = int(str(num), 8)
  tmp = Base_10_to_n(int(tmp), 9)
  num = ''
  for j in range(0, len(tmp)):
    if tmp[j] == '8':
      num += '5'
    else:
      num += tmp[j]
  num = int(num)
print(num)
