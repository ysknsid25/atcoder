a,b,c = map(int, input().split())
goal=10**6+1
for i in range(1, goal):
  ans = i*a%b
  if ans==c:
    print('YES')
    exit()
print('NO')