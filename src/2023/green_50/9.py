n=int(input())

count = 0
for i in range(1,n+1):
  strn = str(i)
  stroct = oct(i)
  if strn.find("7") > -1 or stroct.find("7") > -1:
    count += 1
    continue

ans=n-count
print(ans)