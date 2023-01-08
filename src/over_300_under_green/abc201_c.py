s=list(input())
o=[]
n=[]
for i in range(10):
  c=s[i]
  if c=="o":
    o.append(str(i))
  elif c=="x":
    n.append(str(i))

ans=0
for num in range(10000):
  isValid=True
  strnum=str(num)
  strnum=strnum.zfill(4)
  for check_num in o:
    if not check_num in strnum:
      isValid=False
      break
  for check_num in n:
    if check_num in strnum:
      isValid=False
      break
  if isValid:
    ans+=1
print(ans)  
