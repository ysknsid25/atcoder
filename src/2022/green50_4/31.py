n,k=map(int,input().split())
r,s,p=map(int,input().split())
l=list(input())

score = 0
bfr = []
for i in range(n):
  t = l[i]
  kt = ""
  if i >= k:
    kt = bfr[i-k]
  if t == "r":
    if kt == "p":
      bfr.append("")
    else:
      bfr.append("p")
      score += p
  elif t=="p":
    if kt == "s":
      bfr.append("")
    else:
      bfr.append("s")
      score += s
  else:
    if kt == "r":
      bfr.append("")
    else:
      bfr.append("r")
      score += r
print(score)