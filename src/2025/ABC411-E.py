
def main():
    MOD = 998244353

    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    events = []
    for i in range(N):
        for x in A[i]:
            events.append((x, i))
    
    events.sort()

    counts = [0] * N
    num_zeros = N
    p_le_num = 0
    ans = 0
    u_prev = 0

    invs = [0] * 7
    for i in range(1, 7):
        invs[i] = pow(i, MOD - 2, MOD)
    
    inv6_N = pow(pow(6, N, MOD), MOD - 2, MOD)

    event_idx = 0
    while event_idx < len(events):
        u_curr = events[event_idx][0]
        
        if u_curr > u_prev:
            p_le_prev = (p_le_num * inv6_N) % MOD
            term = ((u_curr - u_prev) % MOD) * ((1 - p_le_prev + MOD) % MOD) % MOD
            ans = (ans + term) % MOD
        
        u_prev = u_curr

        updates = {}
        while event_idx < len(events) and events[event_idx][0] == u_curr:
            _, dice_idx = events[event_idx]
            updates[dice_idx] = updates.get(dice_idx, 0) + 1
            event_idx += 1

        if p_le_num != 0:
            for dice_idx, num_added in updates.items():
                old_count = counts[dice_idx]
                new_count = old_count + num_added
                p_le_num = (p_le_num * invs[old_count]) % MOD
                p_le_num = (p_le_num * new_count) % MOD
                counts[dice_idx] = new_count
        else:
            for dice_idx, num_added in updates.items():
                old_count = counts[dice_idx]
                new_count = old_count + num_added
                counts[dice_idx] = new_count
                if old_count == 0 and new_count > 0:
                    num_zeros -= 1
            
            if num_zeros == 0:
                p_le_num = 1
                for c in counts:
                    p_le_num = (p_le_num * c) % MOD

    print(ans)

if __name__ == "__main__":
    main()
