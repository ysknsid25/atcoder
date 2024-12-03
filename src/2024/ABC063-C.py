n=int(input())
q=[int(input()) for _ in range(n)]
sorted_q = sorted(q)
max_score=sum(q)

if max_score%10 == 0:
  for score in sorted_q:
    if score%10 != 0:
      print(max_score-score)
      exit()
  print(0)
else:
  print(max_score)