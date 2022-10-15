n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

visited = [-1] * (n+1)
visited[1] = 0

now_town = 1
move_cnt = 0
cycle = 1

# 途中から始まる、同じ街をぐるぐるし始めるタイミングを探しつつ、
# その間に計算が終わってしまった場合は終了
for i in range(10 ** 6):
  move_cnt += 1
  now_town = a[now_town]
  if move_cnt == k:
    print(now_town)
    exit()

  if visited[now_town] == -1:
    visited[now_town] = move_cnt
  else:
    cycle = move_cnt - visited[now_town]
    break    

remain = (k - move_cnt) % cycle
for i in range(remain):
  now_town = a[now_town]

print(now_town)