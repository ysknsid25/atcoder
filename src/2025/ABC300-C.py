H,W=map(int,input().split())
C=[list(input()) for _ in range(H)]
N=min(H,W)
ans=[0 for _ in range(N+1)]

for i in range(H):
  for j in range(W):
    res=0
    for d in range(50):
      c=C[i][j]
      if c=='.':
        break
      if i-d < 0 or j-d < 0 or i+d >= H or j+d >= W:
        break
      if C[i+d][j+d] == '#' and C[i+d][j-d] == '#' and C[i-d][j+d] == '#' and C[i-d][j-d] == '#':
        res=d+1
      else:
        break
    if res-1>0:
      ans[res-1]+=1

# ansの1~N+1までの要素を空白区切りで出力
print(" ".join(map(str, ans[1:])))
