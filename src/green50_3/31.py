n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())

score = 0
before = []
for i in range(n):
  te = t[i]
  already = ""
  if i-k >= 0:
    already = before[i-k]
  if te=="r":
    if already != "p":
      before.append("p")
      score += p
    else:
      before.append("")
  elif te=="s":
    if already != "r":
      before.append("r")
      score += r
    else:
      before.append("")
  else:
    if already != "s":
      before.append("s")
      score += s
    else:
      before.append("")

print(score)