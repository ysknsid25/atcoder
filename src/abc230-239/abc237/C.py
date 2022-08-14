def judge():
  S = input()
  # lstrip = 左から指定した文字を取り除く。ただし左の頭から連続した文字の場合に限る
  l = len(S) - len(S.lstrip('a'))
  r = len(S) - len(S.rstrip('a'))
  # 先頭にしかaはつけられないので、左のほうがaが多く続いていた場合はくっつけられない
  if l > r: return False
  T = "a" * (r - l) + S
  return T == T[::-1]

print("Yes" if judge() else "No")
