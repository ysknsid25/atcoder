n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

scores = [0] * n

for j in range(m):
    count_0 = 0
    for i in range(n):
        if s[i][j] == '0':
            count_0 += 1
    count_1 = n - count_0
    if count_0 == 0 or count_1 == 0:
        for i in range(n):
            scores[i] += 1
    elif count_0 < count_1:
        for i in range(n):
            if s[i][j] == '0':
                scores[i] += 1
    else:
        for i in range(n):
            if s[i][j] == '1':
                scores[i] += 1

max_score = max(scores)
winners = []
for i in range(n):
    if scores[i] == max_score:
        winners.append(str(i + 1))

print(" ".join(winners))

