"""
マンハッタン距離
  (x1,y1)と(x2,y2)のマンハッタン距離は、(|x1-x2|,|y1-y2|)
チェビシェフ距離
  (x1,y1)と(x2,y2)のチェビシェフ距離は、max(|x1-x2|,|y1-y2|)
マンハッタン距離→チェビシェフ距離への変換
  (x1,y1)と(x2,y2)のマンハッタン距離=(x1+y1,x1-y1),(x2+y2,x2-y2)間のチェビシェフ距離
"""

n=int(input())
dx=[]
dy=[]
for i in range(n):
  x,y=map(int,input().split())
  ax,ay=x+y,x-y
  dx.append(ax)
  dy.append(ay)
ansx=abs(max(dx)-min(dx))
ansy=abs(max(dy)-min(dy))
print(max(ansx,ansy))