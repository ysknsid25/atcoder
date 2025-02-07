n,d,k=map(int, input().split())
LR=[list(map(int, input().split())) for _ in range(d)]
ST=[list(map(int, input().split())) for _ in range(k)]

ans=[]

for s,t in ST:
  is_right=t-s>0
  for i in range(d):
    l,r=LR[i]
    # 今日は今いる街から移動できるか
    if l<=s<=r:
      # 移動できるなら目的地に一番近いところまで行く
      # 目的地より先に到達できそうなら、その日がゴールになる
      if is_right:
        s=r
        if s>=t:
          ans.append(i+1)
          break
      else:
        s=l
        if s<=t:
          ans.append(i+1)
          break

for a in ans:
  print(a)