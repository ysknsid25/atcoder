n = int(input())
s = list(input())

pos_a = [i for i, char in enumerate(s) if char == 'A']
pos_b = [i for i, char in enumerate(s) if char == 'B']

cost1 = 0
for i in range(n):
    target_pos = 2 * i
    cost1 += abs(pos_a[i] - target_pos)

cost2 = 0
for i in range(n):
    target_pos = 2 * i
    cost2 += abs(pos_b[i] - target_pos)

print(min(cost1, cost2))
