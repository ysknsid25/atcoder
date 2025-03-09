import bisect
from collections import defaultdict

n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

searched = defaultdict(int)
gastronomy_list = [A[0]]
whose_gastronomy = {}
whose_gastronomy[A[0]] = 0
current_min = A[0]
total_min = A[0]

# 左から順に、その時点で一番小さい閾値の美食家がどの位置にいるか？を探す
# [美食度, 位置]として配列に突っ込んでいく
# あとはその寿司が誰に食べられるか？を二分探索する
for i in range(1, n):
    if searched[i]==1:
        continue
    if A[i] < current_min:
        current_min = A[i]
        gastronomy_list.append(A[i])
        whose_gastronomy[A[i]] = i
        total_min = A[i]
    searched[i] = 1

gastronomy_list.sort()
print(whose_gastronomy)

for b in B:
    if b < total_min:
        print(-1)
        continue
    who = bisect.bisect_right(gastronomy_list, b)
    print(who, b)
    if who==0:
        print(whose_gastronomy[gastronomy_list[0]]+1)
    else:
        print(whose_gastronomy[gastronomy_list[who-1]]+1)