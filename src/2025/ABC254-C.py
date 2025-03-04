N,K=[int(nk) for nk in input().split()]
# 全体の長さを Kの倍数に調整
A=[int(a) for a in input().split()]+[10**10]*(K-N%K)
X=[[] for _ in range(K)]

# 入れ替え可能グループに分類
for i in range(N+(K-N%K)):
    X[i%K].append(A[i])

# 各グループごとに昇順にソート
for i in range(K):
    X[i]=sorted(X[i])
    
# 直前の値
prev=0
# 全体が昇順か判定
for column in zip(*X):
    for a in column:
        if prev>a:
            print("No")
            exit()

        prev=a

print("Yes")
