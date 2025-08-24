import collections


def solve():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    start_pos = None
    goal_pos = None
    for r in range(H):
        for c in range(W):
            if A[r][c] == 'S':
                start_pos = (r, c)
            elif A[r][c] == 'G':
                goal_pos = (r, c)

    q = collections.deque([(start_pos[0], start_pos[1], 0)])

    dist = [[[-1] * 2 for _ in range(W)] for _ in range(H)]
    dist[start_pos[0]][start_pos[1]][0] = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c, door_state = q.popleft()

        if (r, c) == goal_pos:
            print(dist[r][c][door_state])
            return

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not (0 <= nr < H and 0 <= nc < W):
                continue

            next_cell = A[nr][nc]
            
            if next_cell == '#':
                continue

            if (next_cell == 'x' and door_state == 0) or \
               (next_cell == 'o' and door_state == 1):
                continue

            next_door_state = door_state
            if next_cell == '?':
                next_door_state = 1 - door_state

            if dist[nr][nc][next_door_state] == -1:
                dist[nr][nc][next_door_state] = dist[r][c][door_state] + 1
                q.append((nr, nc, next_door_state))

    print(-1)

if __name__ == "__main__":
    solve()


