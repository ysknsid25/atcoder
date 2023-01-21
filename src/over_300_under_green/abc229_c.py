n,w=map(int,input().split())

c=[]
for i in range(n):
  a,b=map(int,input().split())
  c.append([a,b])
c.sort(reverse=True)

ans=0
while w>0:
  for d,g in c:
    if g < w:
      w-=g
      ans+=(d*g)
    else:
      ans+=(d*w)
      w=0
    if w==0:
      break
  #! チーズがなくなったらwに余裕があっても終わり
  break
print(ans)