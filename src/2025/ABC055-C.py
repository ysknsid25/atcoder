n, m = map(int, input().split())
ans = 0

pair_c = m // 2
res = min(n, pair_c)  # S部品とC部品のペアで作れる最大数を計算

ans += res
n -= res  # 使用したS部品を減らす
m -= res * 2  # 使用したC部品を減らす

if m > 0:
    ans += m // 4  # 残ったC部品で作れるロボットの数を計算

print(ans)