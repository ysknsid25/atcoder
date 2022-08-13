h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
At = list(zip(*a))
for r in At:
    print(*r)