"""
点(x,y)を角度θだけ反時計回りに回転させた点の座標は以下のように計算できる。
X = x * cosθ - y * sinθ
Y = x * sinθ + y * cosθ
"""
from math import sin,cos,pi

n = int(input())
x0,y0 = map(int,input().split())
x2,y2 = map(int,input().split())
cx=(x0+x2)/2
cy=(y0+y2)/2

#! 中心へ座標を移動
x0-=cx
y0-=cy

#! θぶん反時計回りさせた後の座標を計算する
x1=x0*cos(2*pi/n)-y0*sin(2*pi/n)
y1=x0*sin(2*pi/n)+y0*cos(2*pi/n)

#! 中心へ移動していた分の座標を元に戻す
x1 += cx
y1 += cy

print(x1,y1)