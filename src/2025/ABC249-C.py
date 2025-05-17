
def evaluate(bit, N, K, S):
    res = 0

    # num[c] := 文字 c (0〜25 で表す) の登場回数
    num = [0] * 26
    for i in range(N):
        # bit に S[i] が含まれないならスキップ
        if not (bit & (1 << i)):
            continue

        # S[i] に含まれる文字をカウントしていく
        for c in S[i]:
            num[ord(c) - ord('a')] += 1

    # num[c] = K となる文字 c を数える
    for c in range(26):
        if num[c] == K:
            res += 1

    return res

def main():
    N, K = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    # ビット全探索
    res = 0
    for bit in range(1 << N):
        res = max(res, evaluate(bit, N, K, S))
    
    print(res)

if __name__ == "__main__":
    main()