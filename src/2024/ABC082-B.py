# 入力
s=list(input())
t=list(input())

# sを辞書順最小に
s.sort()
s=''.join(s)

# tを辞書順最大に
t.sort()
t.reverse()
t=''.join(t)

if s<t:
  print('Yes')
else:
  print('No')