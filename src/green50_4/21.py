a,b,w=map(int,input().split())
minx = 10**15
maxx = -10**15

for x in range(1,10**6+1):
  if a*x <= 1000*w <= b*x:
    minx = min(minx,x)
    maxx = max(maxx,x)

if minx==10**15:
  print("UNSATISFIABLE")
else:
  print(minx,maxx)