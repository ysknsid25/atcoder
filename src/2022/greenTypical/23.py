import itertools
n=int(input())
spans=[]
for i in range(n):
  t,l,r=map(int,input().split())
  if t==2:
    r-=0.1
  elif t==3:
    l+=0.1
  elif t==4:
    r-=0.1
    l+=0.1
  spans.append([l,r])

ans=0
for a,b in itertools.combinations(spans, 2):
  al,ar=a
  bl,br=b
  if al<=bl<=ar:
    ans+=1
  elif al<=br<=ar:
    ans+=1
  elif bl<=al<=br:
    ans+=1
  elif bl<=ar<=br:
    ans+=1
print(ans)