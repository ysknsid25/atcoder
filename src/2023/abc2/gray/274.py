n=int(input())
a=[0] + list(map(int, input().split()))

ans=[0]*(2*n+2)

for i in range(1, n+1):
    ans[i*2] = ans[a[i]]+1
    ans[i*2+1] = ans[a[i]]+1

for i in range(1,2*n+2):
    print(ans[i])