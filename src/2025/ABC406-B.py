N, K = map(int, input().split())
A = list(map(int, input().split()))

# 電卓の初期値
current = 1
limit = 10 ** K  # K桁を超える値の閾値

for i in range(N):
    current *= A[i]
    if current >= limit:
        current = 1  # K+1桁以上になる場合は1にリセット

print(current)