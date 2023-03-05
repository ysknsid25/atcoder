n, q = map(int,input().split())

A = list(map(int, input().split()))

L = []
R = []
V = []
for i in range(q):
    l, r, v = map(int,input().split())
    l -= 1
    r -= 1
    L.append(l)
    R.append(r)
    V.append(v)

ans = 0
B = []
for i in range(n-1):
    B.append(A[i+1] - A[i])
    ans += abs(B[i])
else:
    B.append(0)

for i in range(q):
    before = abs(B[L[i]-1]) + abs(B[R[i]])
    if L[i] >= 2:
        B[L[i]-1] += V[i]
    if R[i] <= n-1:
        B[R[i]] -= V[i]
    after = abs(B[L[i]-1]) + abs(B[R[i]])

    ans += after - before

    print(ans)