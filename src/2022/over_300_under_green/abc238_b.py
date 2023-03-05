n=int(input())
seq=set()
cut=list(map(int,input().split()))
t=0
seq.add(0)
seq.add(360)
for point in cut:
  t+=point
  mod=t%360
  seq.add(mod)

seq=list(seq)
seq.sort()
ans=-1
for i in range(1,len(seq)):
  diff=seq[i]-seq[i-1]
  ans=max(ans, diff)
print(ans)