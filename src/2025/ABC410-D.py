import sys

sys.setrecursionlimit(2500) 

def solve():
    N, M = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))

    xor_to_root = [-1] * (N + 1)
    
    color = [0] * (N + 1)
    basis = []

    def add_to_basis(val):
        for b_val in basis:
            val = min(val, val ^ b_val)
        if val > 0:
            basis.append(val)

    def dfs(u, current_path_xor):
        color[u] = 1 
        xor_to_root[u] = current_path_xor

        for v, weight_uv in adj[u]:
            if color[v] == 0:
                dfs(v, current_path_xor ^ weight_uv)
            
            if xor_to_root[v] != -1: 
                cycle_candidate = current_path_xor ^ weight_uv ^ xor_to_root[v]
                add_to_basis(cycle_candidate)
        
        color[u] = 2

    dfs(1, 0)

    if xor_to_root[N] == -1:
        print("-1")
    else:
        min_total_xor = xor_to_root[N]
        for b_val in basis:
            min_total_xor = min(min_total_xor, min_total_xor ^ b_val)
        print(min_total_xor)

if __name__ == "__main__":
    solve()
