def main():
    N = int(input())
    rem = set(range(1, 2 * N + 2))
    while True:
        print(rem.pop(), flush=True)
        a = int(input())
        if a == 0:
            break
        rem.discard(a)


if __name__ == '__main__':
    main()
