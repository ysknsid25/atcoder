from math import sin,cos,pi 
n=int(input())
x0,y0=map(int,input().split())
xn,yn=map(int,input().split())
cx=(x0+xn)/2
cy=(y0+yn)/2
x0-=cx
y0-=cy
x1=cos(2*pi/n)*x0-sin(2*pi/n)*y0
y1=sin(2*pi/n)*x0+cos(2*pi/n)*y0
x1+=cx
y1+=cy
print(x1,y1)