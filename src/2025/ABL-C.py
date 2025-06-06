from collections import defaultdict, deque


def minimum_roads_to_connect_all_cities(N, M, roads):
    # グラフの構築
    graph = defaultdict(list)
    for A, B in roads:
        graph[A].append(B)
        graph[B].append(A)

    # 都市の訪問状況を管理するリスト
    visited = [False] * (N + 1)

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    # 連結成分の数を数える
    connected_components = 0
    for city in range(1, N + 1):
        if not visited[city]:
            bfs(city)
            connected_components += 1

    # 必要な道路の数は連結成分の数 - 1
    return connected_components - 1

if __name__ == "__main__":
    # 入力の受け取り
    N, M = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(M)]

    # 結果の出力
    result = minimum_roads_to_connect_all_cities(N, M, roads)
    print(result) 