
def read_ints():
    return list(map(int, input().split()))

def main():
    input()  # 空行を読み飛ばす
    qs = read_ints()
    as_ = read_ints()
    bs = read_ints()

    max_qs = max(qs)
    result = []

    for i in range(max_qs + 1):
        qs_prime = [q - i * a for q, a in zip(qs, as_)]
        if all(q >= 0 for q in qs_prime):
            j = min((q // b for q, b in zip(qs_prime, bs) if b != 0), default=0)
            result.append(i + j)

    print(max(result))

if __name__ == "__main__":
    main()