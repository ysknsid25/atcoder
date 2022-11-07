n = list(input())

sum = 0
zero = 0
one = 0
two = 0
for i in range(len(n)):
  num = int(n[i])
  sum += num
  mod = num%3
  if mod==0:
    zero += 1
  elif mod==1:
    one += 1
  else:
    two += 1

if sum < 3:
  print(-1)
  exit()

mod = sum%3
if mod==0:
  print(0)
elif mod==1:
  if one > 0:
    if len(n) <= 1:
      print(-1)
    else:
      print(1)
  else:
    if len(n) <= 2:
      print(-1)
    else:
      print(2)
elif mod==2:
  if two > 0:
    if len(n) <= 1:
      print(-1)
    else:
      print(1)
  else:
    if len(n) <= 2:
      print(-1)
    else:
      print(2)
else:
  print(-1)