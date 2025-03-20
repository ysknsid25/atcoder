from collections import deque

n = int(input())
s = input()

d = deque([i for i in range(n) if s[i] == "1"])
ans = 0
# 両端の1を中央に交互に寄せていく
# 最後に今の位置に来るまでにあった1の数だけ移動しないとダメなので、掛けてあげる必要がある
cnt_front, cnt_back = 0, 0
while len(d) > 1:
    if cnt_front <= cnt_back:
        now = d.popleft()
        cnt_front += 1
        target = d[0]
        dist = target - now - 1
        ans += dist * cnt_front
    else:
        now = d.pop()
        cnt_back += 1
        target = d[-1]
        dist = now - target - 1
        ans += dist * cnt_back

print(ans)
