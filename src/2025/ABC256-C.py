def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    table = [0] * 9
    mx = max(h1, h2, h3, w1, w2, w3)

    ans = 0
    for a in range(1, mx):
        table[0] = a
        for b in range(1, mx):
            table[1] = b
            table[2] = h1 - table[0] - table[1]

            if table[2] < 1:
                continue

            for c in range(1, mx):
                table[3] = c
                for d in range(1, mx):
                    table[4] = d
                    table[5] = h2 - table[3] - table[4]
                    table[6] = w1 - table[0] - table[3]
                    table[7] = w2 - table[1] - table[4]
                    table[8] = h3 - table[6] - table[7]

                    if table[5] < 1 or table[6] < 1 or table[7] < 1 or table[8] < 1:
                        continue

                    if (table[0] + table[1] + table[2] == h1 and
                        table[3] + table[4] + table[5] == h2 and
                        table[6] + table[7] + table[8] == h3 and
                        table[0] + table[3] + table[6] == w1 and
                        table[1] + table[4] + table[7] == w2 and
                        table[2] + table[5] + table[8] == w3):
                        ans += 1

    print(ans)

if __name__ == "__main__":
    main()
