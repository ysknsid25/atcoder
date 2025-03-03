s=list(input())
k=int(input())
one=0
ans=-1
for i in range(len(s)):
  if s[i]=="1":
    one+=1
  else:
    ans=s[i]
    break
if k<=one:
  print(1)
else:
  print(s[one])