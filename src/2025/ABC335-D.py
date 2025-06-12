dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def main():
    N = int(input())
    board = [["" for _ in range(N)] for _ in range(N)]
    board[N // 2][N // 2] = "T"

    def inside(y, x):
        return 0 <= y < N and 0 <= x < N

    current = 1
    y, x, d = 0, 0, 0
    board[0][0] = str(current)

    while current + 1 < N * N:
        ny = y + dy[d]
        nx = x + dx[d]
        if inside(ny, nx) and board[ny][nx] == "":
            current += 1
            y, x = ny, nx
            board[y][x] = str(current)
        else:
            d = (d + 1) % 4

    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    main()
