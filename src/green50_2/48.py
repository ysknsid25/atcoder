"""
マンハッタン距離
  (x1,y1)と(x2,y2)のマンハッタン距離は、|x1-x2|+|y1-y2|
チェビシェフ距離
  (x1,y1)と(x2,y2)のチェビシェフ距離は、max(|x1-x2|,|y1-y2|)
マンハッタン距離→チェビシェフ距離への変換
  (x1,y1)と(x2,y2)のマンハッタン距離=(x1+y1,x1-y1),(x2+y2,x2-y2)間のチェビシェフ距離
"""
n=int(input())
chevi_x=[]
chevi_y=[]
for i in range(n):
  x,y=map(int,input().split())
  #! チェビシェフ距離の座標を算出する際にはそのまま加算減算する
  tmp_x=x+y
  tmp_y=x-y
  chevi_x.append(tmp_x)
  chevi_y.append(tmp_y)
dist_chevi_x=abs(max(chevi_x)-min(chevi_x))
dist_chevi_y=abs(max(chevi_y)-min(chevi_y))
ans=max(dist_chevi_x,dist_chevi_y)
print(ans)