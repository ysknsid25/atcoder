from collections import deque
h, w = map(int, input().split())
s = []
for i in range(h):
    tmp = list(input())
    s.append(tmp)

ud_list = [0, 1, -1]
lr_list = [0, 1, -1]
ans = -1
for sh in range(h):
    for sw in range(w):
        start = s[sh][sw]
        if start == "#":
            continue
        steps = [[-1 for i in range(w)] for i in range(h)]
        steps[sh][sw] = 0
        que = deque()
        que.append([sh, sw])
        while len(que) > 0:
            nowh, noww = que.popleft()
            for ud in ud_list:
                for lr in lr_list:
                    if ud == 0 and lr == 0:
                        continue
                    if abs(ud)+abs(lr) == 2:
                        continue
                    nxth = nowh+ud
                    nxtw = noww+lr
                    if nxth < 0 or nxth > h-1 or nxtw < 0 or nxtw > w-1:
                        continue
                    if s[nxth][nxtw] == "#":
                        continue
                    if sh == nxth and sw == nxtw:
                        continue
                    if steps[nxth][nxtw] <= 0:
                        steps[nxth][nxtw] = steps[nowh][noww]+1
                        que.append([nxth, nxtw])
        res = -1
        for i in range(h):
            res = max(res, max(steps[i]))
        ans = max(ans, res)

print(ans)
