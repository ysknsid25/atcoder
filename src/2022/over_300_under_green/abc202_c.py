n=int(input())
a=list(map(int,input().split()))
b=[0]+list(map(int,input().split()))
c=[0]+list(map(int,input().split()))

memo=[0 for i in range(n+1)]
for c_num in c:
  b_num=b[c_num]
  memo[b_num]+=1

ans=0
for a_num in a:
  ans+=memo[a_num]
print(ans)