import sys

# 再帰の上限を増やす
sys.setrecursionlimit(10**6)

class UnionFind:
    """
    Union-Find木の実装。
    各連結成分における黒い頂点の数を管理する機能を持つ。
    """
    def __init__(self, n):
        # 親要素のノード番号を格納。親がない場合は-(その集合のサイズ)
        self.parent = [-1] * (n + 1)
        # 各連結成分の黒い頂点の数を格納
        self.black_counts = [0] * (n + 1)

    def find(self, x):
        """xが属する集合の根を返す（経路圧縮あり）"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        """xとyが属する集合を併合する"""
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False
        
        # サイズが大きい方にマージする (union by size)
        if self.parent[x_root] > self.parent[y_root]:
            x_root, y_root = y_root, x_root
        
        self.parent[x_root] += self.parent[y_root]
        self.parent[y_root] = x_root
        # 黒い頂点の数をマージ
        self.black_counts[x_root] += self.black_counts[y_root]
        return True

    def get_black_count(self, x):
        """xが属する連結成分の黒い頂点の数を返す"""
        root = self.find(x)
        return self.black_counts[root]

def main():
    """
    メイン処理
    """
    try:
        # 高速な入力
        input = sys.stdin.readline
        
        N, Q = map(int, input().split())
        
        # Union-Find木を初期化
        uf = UnionFind(N)
        
        # 各頂点の色を管理 (0: 白, 1: 黒)
        colors = [0] * (N + 1)

        # クエリ処理
        for _ in range(Q):
            query = list(map(int, input().split()))
            
            query_type = query[0]
            
            if query_type == 1:
                # タイプ1: 辺の追加
                u, v = query[1], query[2]
                uf.union(u, v)
                
            elif query_type == 2:
                # タイプ2: 色の変更
                v = query[1]
                root_v = uf.find(v)
                
                if colors[v] == 0:  # 白 -> 黒
                    colors[v] = 1
                    uf.black_counts[root_v] += 1
                else:  # 黒 -> 白
                    colors[v] = 0
                    uf.black_counts[root_v] -= 1
                    
            elif query_type == 3:
                # タイプ3: 到達可能性の判定
                v = query[1]
                if uf.get_black_count(v) > 0:
                    print("Yes")
                else:
                    print("No")

    except (IOError, IndexError):
        # 入力例2のような空の入力に対応
        # また、その他の予期せぬ入力エラーもここで捕捉
        pass

if __name__ == "__main__":
    main()
