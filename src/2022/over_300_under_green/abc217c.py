n=int(input())
p=list(map(int,input().split()))
q=[0 for i in range(n)]

for i in range(n):
  qi=p[i]-1
  q[qi]=i+1

#! 配列の頭に*をつけると角カッコとカンマなしで出力してくれる
print(*q)