from collections import deque

atcoder = "atcoder"

def main():
    S = input().strip()

    # BFS のためのデータ構造
    queue = deque()
    dist = {}

    # 初期条件
    queue.append(S)
    dist[S] = 0

    # BFS
    while queue:
        v = queue.popleft()
        
        for i in range(len(atcoder) - 1):
            v2 = list(v)
            v2[i], v2[i+1] = v2[i+1], v2[i]
            v2_str = ''.join(v2)
            if v2_str not in dist:
                queue.append(v2_str)
                dist[v2_str] = dist[v] + 1

    print(dist[atcoder])

if __name__ == "__main__":
    main()
