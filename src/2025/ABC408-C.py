def min_turrets_to_destroy(n, m, intervals):
    # 壁ごとの守られている砲台の数をカウント
    wall_count = [0] * (n + 1)
    for l, r in intervals:
        wall_count[l] += 1
        if r + 1 <= n:
            wall_count[r + 1] -= 1

    # 累積和を計算して各壁の守られている砲台の数を求める
    for i in range(1, n + 1):
        wall_count[i] += wall_count[i - 1]

    # 最小値を求める
    return min(wall_count[1:])

# 入力
n, m = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(m)]

# 出力
print(min_turrets_to_destroy(n, m, intervals))