T = int(input())
for _ in range(T):
  N = int(input())
  S = list(input())
  # 文字列の長さが1は例外
  if(N == 1):
    print(S[0])
    continue
  
  # 左から順番に大きい文字を見つける
  for i in range(N-1):
    if(S[i] > S[i+1]):
      break
  
  # 見つけた大きい文字より大きい右の文字を見つける
  j = N
  for _j in range(i+1, N):
    if(S[_j] > S[i]):
      j = _j
      break
  
  # 文字の順番を変える
  T = S[:i] + S[i+1:j] + S[i:i+1] + S[j:N]
  
  print("".join(T))
  