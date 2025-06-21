

def main():
    N, Q = map(int, input().split())
    is_black = [False] * (N + 2)
    count = 0
    queries = list(map(int, input().split()))
    for line in queries:
        A = int(line)
        if is_black[A]:
            if not is_black[A-1]:
                count -= 1
            if is_black[A+1]:
                count += 1
        else:
            if not is_black[A-1]:
                count += 1
            if is_black[A+1]:
                count -= 1
        is_black[A] = not is_black[A]
        print(count)

if __name__ == "__main__":
    main()
