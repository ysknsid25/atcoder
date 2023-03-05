n=int(input())
k=3
yestrday = -1
dp = [[0 for i in range(k)] for i in range(n)]

#! 初日
hp = list(map(int,input().split()))
dp[0][0] = hp[0]
dp[0][1] = hp[1]
dp[0][2] = hp[2]

#! 二日目以降
for i in range(1,n):
  hp = list(map(int,input().split()))
  #! 昨日の選択
  for j in range(k):
    #! 今日の選択
    for l in range(k):
      #! 昨日選んだもの以外を今日は選ぶことができる
      if j != l:
        #! 今日aを選んだ時の幸福度は、昨日bかcを選んだ場合+今日aを選んだ場合の幸福度の大きい方となる
        dp[i][j] = max(dp[i][j], dp[i-1][l] + hp[j])

res = dp[n-1]
ans = max(res)
print(ans)
