n,m=map(int,input().split())
blues=[0] + list(map(int,input().split())) + [n+1]
sorted_blues=sorted(blues)

res=[]
min_diff=n
for i in range(len(sorted_blues)-1):
  diff=sorted_blues[i+1]-sorted_blues[i]-1
  if diff>0:
    res.append(diff)
    min_diff=min(min_diff,diff)

ans = 0
for r in res:
  ans += (r + min_diff - 1) // min_diff

print(ans)