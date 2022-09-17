# 2進数aに対する部分集合の列挙を取得する典型パターン
# 7行目からが肝

n = int(input())
ans = []
s = n
while(True):
  ans.append(s)
  if s == 0: break
  s = (s - 1) & n

ans.sort()
for i in ans:
  print(i)
