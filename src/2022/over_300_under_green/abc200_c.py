n=int(input())
a=list(map(int,input().split()))
mod_list=[x%200 for x in a]

#! こう書きたいところだけど、そうするとn*nが最大計算量になりTLE
# ans=0
# for i in range(n-1):
#   for j in range(n):
#     if mod_list[i]==mod_list[j]:
#       ans+=1
# print(ans)

#! そこで200で割った時のあまりの数の出現回数をカウントする
#! 1回だけだと0なので、2回目以降に現れた時に答えとしてカウント
ans=0
cnt=[0 for i in range(201)]
for mod in mod_list:
  ans+=cnt[mod]
  cnt[mod]+=1
print(ans)