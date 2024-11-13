from collections import deque

q=int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
que=deque()

for query in queries:
    if query[0] == 1:
        a, b, c = query
        que.append([b, c])
    else:
      res = 0
      a, c = query
      before = c
      while before > 0:
        que_x, que_c = que[0]
        after = before - que_c
        if after > 0:
          res+=(que_x*que_c)
          que.popleft()
        else:
          res+=(que_x*before)
          que[0] = [que_x, abs(after)]
        before = after
      print(res)