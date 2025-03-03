n = int(input())
h = list(map(int, input().split()))
ans = 0

while max(h) > 0:  # すべての花が 0 になるまで繰り返す
    i = 0
    while i < n:
        if h[i] > 0:  # 高さが 0 以上の区間を見つける
            ans += 1
            while i < n and h[i] > 0:
                h[i] -= 1  # その区間を1減らす
                i += 1
        i += 1  # 0 の部分はスキップ

print(ans)