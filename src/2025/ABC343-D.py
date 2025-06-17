from collections import defaultdict

n,t=map(int, input().split())
scores=[0 for _ in range(n)]
dict_scores = defaultdict(int)
dict_scores[0]=n
ans=1
for i in range(t):
    a,b=map(int, input().split())
    before_score = scores[a-1]
    new_score = before_score + b
    if dict_scores[new_score] == 0:
        ans += 1
    dict_scores[before_score] -= 1
    if dict_scores[before_score] == 0:
        ans -= 1
    dict_scores[new_score] += 1
    scores[a-1] = new_score
    print(ans)


