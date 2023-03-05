n, k = map(int, input().split())
scores = []
for i in range(0, n):
  ta, tb = map(int, input().split())
  scores.append(ta-tb)
  scores.append(tb)

scores.sort(reverse=True)

ans = 0
for i in range(k):
  score = scores[i]
  ans += score

print(ans)