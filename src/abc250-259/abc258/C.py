n, q = map(int, input().split())
s = input()

t = 0
for i in range(0, q):
    query = input().split()
    direct = query[0]
    posi = int(query[1])
    if direct == '1':
      t = (t - posi+n)%n
    else:
        print(s[(t + posi-1)%n])
