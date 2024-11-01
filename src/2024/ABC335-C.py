n,q = map(int, input().split())
p = []
for i in range(n):
  p.append([i+1, 0])
p.sort(reverse=True)

move_count = 0
for i in range(q):
  a, b = input().split()
  if a == '1':
    x, y = p[n-1+move_count]
    if b == 'U':
      p.append([x, y+1])
    elif b == 'D':
      p.append([x, y-1])
    elif b == 'L':
      p.append([x-1, y])
    elif b == 'R':
      p.append([x+1, y])
    move_count+=1
  else:
    b = int(b)
    print(p[n-1+move_count-b+1][0], p[n-1+move_count-b+1][1])