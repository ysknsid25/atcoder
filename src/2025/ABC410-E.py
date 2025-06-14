def solve():
    N, H, M = map(int, input().split())
    monsters = []
    for _ in range(N):
        monsters.append(list(map(int, input().split())))

    dp = [-1] * (H + 1)
    dp[H] = M

    ans = 0

    for i in range(N):
        A_i, B_i = monsters[i]
        next_dp = [-1] * (H + 1)
        can_defeat_current_monster = False

        for h_before in range(H + 1):
            if dp[h_before] == -1:
                continue
            
            current_magic = dp[h_before]

            if h_before >= A_i:
                h_after = h_before - A_i
                m_after = current_magic
                next_dp[h_after] = max(next_dp[h_after], m_after)
                can_defeat_current_monster = True
            
            if current_magic >= B_i:
                h_after = h_before
                m_after = current_magic - B_i
                next_dp[h_after] = max(next_dp[h_after], m_after)
                can_defeat_current_monster = True

        if not can_defeat_current_monster:
            print(ans)
            return
        
        dp = next_dp
        ans = i + 1

    print(ans)

solve()
