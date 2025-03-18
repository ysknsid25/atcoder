H,W=map(int, input().split())
C=[list(input()) for _ in range(H)]
dp=[[0 for _ in range(W)] for _ in range(H)]
dp[0][0]=1
ans=0
for i in range(H):
    for j in range(W):
        up=i-1
        left=j-1
        # 今の位置が壁ならそこへはいけない
        if C[i][j] == '#':
            dp[i][j]=0
            continue
        # 左から移動できる場合
        if left>=0:
            if dp[i][left] > 0:
              dp[i][j]=max(dp[i][j], dp[i][left]+1)
        if up>=0:
            if dp[up][j] > 0:
              dp[i][j]=max(dp[i][j], dp[up][j]+1)
        ans=max(ans, dp[i][j])

print(ans)
