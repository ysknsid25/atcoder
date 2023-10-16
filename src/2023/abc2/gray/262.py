n=int(input())
a=[0]+list(map(int,input().split()))

ans=0

# ai=iになる要素がいくつあるかを探す。その中から二つ選んだ時の組み合わせが答えの一部
x=0
for i in range(1,n+1):
    if a[i]==i:
        x+=1
ans+=x*(x-1)//2

# ai=jになる要素がいくつあるか探す。a[ai]=iとなり、なおかつi<jであるもの
for i in range(1,n+1):
    j=a[i]
    if a[j]==i and i<j:
        ans+=1

print(ans)