s=input()
l=len(s)
if l == 1:
  print(s)
else:
  mid=(l+1)//2-1
  print(s[mid:mid+1])