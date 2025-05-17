from collections import defaultdict

# 入力の読み込み
H, W, N = map(int, input().split())
garbage_rows = defaultdict(int)
garbage_cols = defaultdict(int)
garbage_positions = defaultdict(set)  # 各行にあるゴミの列位置を記録
garbage_positions_cols = defaultdict(set)  # 各列にあるゴミの行位置を記録

# ゴミの位置を記録
for _ in range(N):
    X, Y = map(int, input().split())
    garbage_rows[X] += 1
    garbage_cols[Y] += 1
    garbage_positions[X].add(Y)
    garbage_positions_cols[Y].add(X)  # 列に対する行の位置を記録

Q = int(input())
queries = [input().split() for _ in range(Q)]

# クエリの処理
for query in queries:
    t, v = int(query[0]), int(query[1])
    if t == 1:  # タイプ1: 行に関するクエリ
        print(garbage_rows[v])
        for col in garbage_positions[v]:  # 行vにあるすべての列を処理
            garbage_cols[col] -= 1
            if garbage_cols[col] == 0:
                del garbage_cols[col]
            garbage_positions_cols[col].remove(v)  # 列の行位置から削除
            if not garbage_positions_cols[col]:
                del garbage_positions_cols[col]
        garbage_rows[v] = 0
        del garbage_positions[v]  # 行vのゴミを削除
    elif t == 2:  # タイプ2: 列に関するクエリ
        print(garbage_cols[v])
        for row in garbage_positions_cols[v]:  # 列vにあるすべての行を処理
            garbage_rows[row] -= 1
            if garbage_rows[row] == 0:
                del garbage_rows[row]
            garbage_positions[row].remove(v)  # 行の列位置から削除
            if not garbage_positions[row]:
                del garbage_positions[row]
        garbage_cols[v] = 0
        del garbage_positions_cols[v]  # 列vのゴミを削除
