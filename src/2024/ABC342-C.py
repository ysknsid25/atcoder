from collections import defaultdict

dict=defaultdict(str)
appeared=defaultdict(int)
n=int(input())
s=list(input())
q=int(input())
for i in range(q):
  c, d=input().split()
  if appeared[c]==0:
    appeared[c]=1
    dict[c]=d
  for k, v in dict.items():
    if v == c:
      dict[k]=d

ans=[]
for c in s:
  if appeared[c]==1:
    ans.append(dict[c])
  else:
    ans.append(c)

print("".join(ans))