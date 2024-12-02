n=int(input())
c=list(input())
ans=0
red=0

for stone in c:
  if stone=='R':
    red+=1

for i in range(red):
  if c[i]=='W':
    ans+=1

print(ans)