N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

range_diff = [0] * (10**6 + 10)

for l, r in LR:
    range_diff[l] += 1
    range_diff[r] -= 1

inside = 0
fr = -1

for i in range(len(range_diff)):
    if inside == 0 and range_diff[i] > 0:
        fr = i  # 範囲の開始を記録
    inside += range_diff[i]
    if inside == 0 and fr != -1:
        print(fr, i)  # 範囲の終了を記録して出力
        fr = -1
