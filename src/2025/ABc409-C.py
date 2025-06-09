import collections


def count_equilateral_triangles(N, L, distances):
    if N < 3:
        return 0

    # 点の位置を計算
    # N=0 の場合: positions = []
    # N=1 の場合: positions = [0]
    # N>1 の場合: positions[0]=0, 残りはループで計算
    positions = [0] * N 
    for i in range(1, N): # N=0, N=1 のときは実行されない
        positions[i] = (positions[i - 1] + distances[i - 1]) % L
    
    # 正三角形を形成するためには、円周 L が3で割り切れる必要がある
    if L % 3 != 0:
        return 0
    
    side_len = L // 3
    
    # L が3の倍数であり、問題の制約から通常 L>=3 が期待されるため side_len >= 1。
    # side_len = 0 (L=0 の場合など) は辺長0の正三角形となり、ここでは0個とする。
    if side_len == 0: 
        return 0

    # 各位置に存在する点の数をカウント
    position_counts = collections.Counter(positions)
    
    count = 0
    # 各位置 p1 を起点として正三角形 (p1, p2_target, p3_target) を探す
    # side_len >= 1 のため、p1, p2_target, p3_target は必ず異なる3つの位置になる
    for p1 in position_counts:
        p2_target = (p1 + side_len) % L
        p3_target = (p1 + 2 * side_len) % L # または (p2_target + side_len) % L

        # p1, p2_target, p3_target の位置に点が存在する場合、その組み合わせをカウント
        # Counter は存在しないキーに対して 0 を返すので、直接積を計算しても安全
        if p2_target in position_counts and p3_target in position_counts:
            count += position_counts[p1] * position_counts[p2_target] * position_counts[p3_target]

    # 各正三角形は、3つの頂点のどれを p1 としたかによって3回カウントされる。
    # (例: 三角形 {A, B, C} は、p1=A, p1=B, p1=C の3回カウントされる)
    # side_len > 0 なので、A, B, C は必ず異なる位置。
    return count // 3

if __name__ == "__main__":
    # 入力を受け取る
    N, L = map(int, input().split())
    
    actual_distances = []
    # distances は N-1 個の要素。N=0 or N=1 の場合は distances は空。
    # N > 1 の場合のみ distances の入力行が存在する。
    if N > 1:
        actual_distances = list(map(int, input().split()))
    
    # 答えを計算して出力
    result = count_equilateral_triangles(N, L, actual_distances)
    print(result)
