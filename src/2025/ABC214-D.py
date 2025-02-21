import heapq

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# ダイクストラ法のための優先度付きキュー
pq = []
for i in range(n):
    heapq.heappush(pq, (t[i], i))  # (現在の最短時間, 頂点)

# ダイクストラ法の実行
while pq:
    time, u = heapq.heappop(pq)  # 現在の最小時間の頂点を取り出す
    
    # 次の頂点 (環状なので (u+1) % n)
    v = (u + 1) % n
    new_time = time + s[u]  # u から v へ行くコストを加算
    
    # より短い時間で v に行ける場合、更新する
    if new_time < t[v]:
        t[v] = new_time
        heapq.heappush(pq, (t[v], v))  # 更新後の情報をキューに追加

# 結果の出力
for i in n:
    print(t[i])
