n = int(input())
h = list(map(int, input().split()))
max_value = max(h)
max_index = h.index(max_value) + 1
print(max_index)
