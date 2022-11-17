def price(a,b,n):
  strn = str(n)
  d = len(strn)
  p = a*n+b*d
  return p

a,b,x=map(int, input().split())
l = 1
r = 10**15

#! a,bがバカデカくてxが小さい時は、1も買えない
if x<price(a,b,1):
  print(0)
  exit()

while r-l > 1:
  mid = (r+l)//2
  midp = price(a,b,mid)
  if midp <= x:
    l = mid
  else:
    r = mid

#! 10**9より大きい時は、10**9が最大で買える整数になる
#! 左が答えになるのは、例えば一番最後がl=28,r=29になった場合//で計算すれば切り捨てとなり、必ず左の値になる
#! よって左が購入できる最も大きな数となるため
if 10**9<l:
  print(10**9)
else:
  print(l)
