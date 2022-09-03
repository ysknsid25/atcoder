# 小さい制約は順列全探索

import itertools
n = int(input())

a = []
for i in range(n):
  tmp = list(map(int, input().split()))
  a.append(tmp);

m = int(input())

xy = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
  x, y = map(int, input().split())
  xy[x-1][y-1] = 1
  xy[y-1][x-1] = 1

runlist = list(itertools.permutations(range(n)))
runlen = len(runlist)

mintime = 1e9
for i in range(0, runlen):
  run = runlist[i]
  frunner = run[0] - 1
  time = a[frunner][0]
  isCorrect = True
  for j in range(1, len(run)):
    before = j - 1
    runner = run[j] - 1
    brunner = run[before] - 1
    if xy[runner][brunner] == 1 or xy[brunner][runner] == 1:
      isCorrect = False
      break
    time += a[runner][j]
  if isCorrect:
    mintime = min(mintime, time)

if mintime == 1e9:
  print(-1)
else:
  print(mintime)