n,m=map(int, input().split())
students = []
check_points = []

for _ in range(n):
  a,b= map(int, input().split())
  students.append((a, b))

for _ in range(m):
  x, y = map(int, input().split())
  check_points.append((x, y))

for i in range(n):
  min_distance=10**9
  ans=-1
  for j in range(m):
    x1, y1 = students[i]
    x2, y2 = check_points[j]
    distance = abs(x1 - x2) + abs(y1 - y2)
    if distance < min_distance:
      min_distance = distance
      ans = j + 1
  print(ans)