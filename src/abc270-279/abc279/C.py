h,w=map(int,input().split())
ahr = []
bhr = []
awc = [0 for i in range(w)]
bwc = [0 for i in range(w)]

for i in range(h):
  cnt = 0
  s = list(input())
  for j in range(w):
    c = s[j]
    if c=="#":
      cnt += 1
      awc[j] += 1
  ahr.append(cnt)

for i in range(h):
  cnt = 0
  t = list(input())
  for j in range(w):
    c = t[j]
    if c=="#":
      cnt += 1
      bwc[j] += 1
  bhr.append(cnt)

awc.sort()
bwc.sort()

if ahr == bhr and awc == bwc:
  print("Yes")
else:
  print("No")