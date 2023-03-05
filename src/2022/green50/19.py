x, k, d = map(int, input().split())
x = abs(x)

pattern = x - (d * k)

if pattern >= 0:
  print(pattern)
else:
  #0を跨ぐ直前の座標までの移動回数
  cnt = x // d
  #0を跨ぐ直前の座標
  before = x - (cnt * d)
  #0を跨いだ直後の座標
  after = abs(x - (cnt * d) - d)
  #残りの移動回数。偶数なら直前、奇数なら直後が答え
  remain = k - cnt
  if remain % 2 == 0:
    print(before)
  else:
    print(after)