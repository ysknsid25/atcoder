import heapq
from collections import defaultdict

count_dict = defaultdict(int)
max_list = []
min_list = []
heapq.heapify(max_list)
heapq.heapify(min_list)

q = int(input())
for _ in range(q):
    query = input()
    if query.startswith('1'):
        _, x = map(int, query.split())
        if count_dict[x] == 0:
            heapq.heappush(max_list, -x)  # 最大値用ヒープ
            heapq.heappush(min_list, x)   # 最小値用ヒープ
        count_dict[x] += 1

    elif query.startswith('2'):
        _, x, c = map(int, query.split())
        if count_dict[x] > 0:
            count_dict[x] -= min(c, count_dict[x])
            if count_dict[x] == 0:
                # max_list と min_list の整合性を保つ
                while max_list and count_dict[-max_list[0]] == 0:
                    heapq.heappop(max_list)
                while min_list and count_dict[min_list[0]] == 0:
                    heapq.heappop(min_list)

    else:
        print(-max_list[0] - min_list[0])


