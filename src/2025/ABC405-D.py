from collections import deque

h, w = map(int, input().split())
s = []
queue = deque()
for i in range(h):
    l = list(input())
    for j in range(w):
        if l[j] == "E":
            queue.append((i, j))
    s.append(l)

# 矢印の方向を定義（来た方向とは逆向き）
dx = [-1, 1, 0, 0]  # 上、下、左、右
dy = [0, 0, -1, 1]
arrows = ["v", "^", ">", "<"]  # 下、上、右、左

# 初期化
ans = [row[:] for row in s]  # deepcopyの代わりにリスト内包表記を使用

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and ans[nx][ny] == '.':
            ans[nx][ny] = arrows[d]  # 来た方向とは逆向きの矢印を設定
            queue.append((nx, ny))

for row in ans:
    print(''.join(row))
