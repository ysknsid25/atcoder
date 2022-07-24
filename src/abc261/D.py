n, m = map(int, input().split())
x = list(map(int, input().split()))
b = {}
for i in range(1, m+1):
    c, y = map(int, input().split())
    b[c] = y

inf = 10 ** 16
score = [[-inf for i in range(n+1)] for j in range(n+1)]
score[0][0] = 0
for i in range(1, n+1):
    for j in range(0, n+1):
        if j == 0:
            score[i][j] = max(score[i - 1])
        else:
            bonus = 0
            if j in b:
                bonus = b[j]
            score[i][j] = score[i - 1][j - 1] + x[(i - 1)] + bonus

ans = max(score[n])

print(ans)
