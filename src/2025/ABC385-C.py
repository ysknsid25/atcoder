# 参考
# https://drken1215.hatenablog.com/entry/2024/12/25/021000
def main():
    N = int(input())
    H = list(map(int, input().split()))

    res = 1

    # 数列の間隔 d を全探索する
    for d in range(1, N):
        # 数列全体を d 個に分割して解く
        for r in range(d):
            # 分割して得られた数列に対して、同じ値が最大何個連続しているかを求める
            num = 1
            prev = -1
            for i in range(r, N, d):
                if H[i] == prev:
                    num += 1
                    res = max(res, num)
                else:
                    num = 1
                    prev = H[i]

    print(res)

if __name__ == "__main__":
    main()
