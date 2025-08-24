N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_sum = 0
for i in range(N):
    total_sum += min(A[i], B[i])
    
for _ in range(Q):
    c, x, v = input().split()
    x = int(x) - 1
    v = int(v)
    
    total_sum -= min(A[x], B[x])
    
    if c == 'A':
        A[x] = v
    else:
        B[x] = v
        
    total_sum += min(A[x], B[x])
    
    print(total_sum)
