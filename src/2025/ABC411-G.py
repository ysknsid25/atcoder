import sys

sys.setrecursionlimit(10**6)

def solve():
    MOD = 998244353

    input_lines = sys.stdin.read().strip().split('\n')
    line_iterator = iter(input_lines)
    
    N, M = map(int, next(line_iterator).split())
    
    adj = [[0] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, next(line_iterator).split())
        u -= 1
        v -= 1
        adj[u][v] += 1
        adj[v][u] += 1


    dp = [[0] * N for _ in range(1 << N)]
    for i in range(N):
        dp[1 << i][i] = 1

    for S in range(1, 1 << N):
        s = (S & -S).bit_length() - 1
        
        for v_idx in range(s, N):
            if not ((S >> v_idx) & 1):
                continue
            if dp[S][v_idx] == 0:
                continue

            for u_idx in range(s + 1, N):
                if not ((S >> u_idx) & 1) and adj[v_idx][u_idx] > 0:
                    next_S = S | (1 << u_idx)
                    dp[next_S][u_idx] = (dp[next_S][u_idx] + dp[S][v_idx] * adj[v_idx][u_idx]) % MOD

    cycles_k3_plus = 0
    for S in range(1, 1 << N):
        if bin(S).count('1') < 3:
            continue
        
        s = (S & -S).bit_length() - 1
        
        for v_idx in range(s + 1, N):
            if not ((S >> v_idx) & 1):
                continue
            
            if adj[v_idx][s] > 0:
                cycles_k3_plus = (cycles_k3_plus + dp[S][v_idx] * adj[v_idx][s]) % MOD

    inv2 = pow(2, MOD - 2, MOD)
    cycles_k3_plus = (cycles_k3_plus * inv2) % MOD

    cycles_k2 = 0
    for i in range(N):
        for j in range(i + 1, N):
            c = adj[i][j]
            if c >= 2:
                cycles_k2 = (cycles_k2 + c * (c - 1) // 2) % MOD
    
    total_cycles = (cycles_k2 + cycles_k3_plus) % MOD
    print(total_cycles)

solve()
