a, b = map(int, input().split())

scores = [4,2,1]
ta = []
for i in range(0, 3):
  score = scores[i]
  if a >= score:
    a -= score
    ta.append(score)
  if b >= score:
    b -= score
    ta.append(score)

res = set(ta)
ans = sum(res)
print(ans)