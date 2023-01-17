n=int(input())
al=[]
bl=[]
ftime=0
for i in range(n):
  a,b=map(int,input().split())
  al.append(a)
  bl.append(b)
  ftime+=a/b

time=ftime/2
dist=0
for i in range(n):
  if al[i]/bl[i]<=time:
    time-=al[i]/bl[i]
    dist+=al[i]
  else:
    dist+=bl[i]*time
    break
print(dist)