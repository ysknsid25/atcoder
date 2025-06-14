import sys


def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    A = [i+1 for i in range(N)]
    offset = 0

    for _ in range(Q):
        query = list(map(int, input().split()))
        query_type = query[0]

        if query_type == 1:
            p, x = query[1], query[2]
            A[(p - 1 + offset) % N] = x
        elif query_type == 2:
            p = query[1]
            print(A[(p - 1 + offset) % N])
        elif query_type == 3:
            k = query[1]
            offset = (offset + k) % N

if __name__ == '__main__':
    main()
    main()
