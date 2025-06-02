N,T=map(int, input().split())
t=list(map(int, input().split()))

ans=0
for i in range(0, N-1):
    ans += min(t[i] + T, t[i+1]) - t[i]
print(ans + T)
