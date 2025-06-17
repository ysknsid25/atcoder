import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

permutations = list(itertools.permutations(range(1, N + 1)))

# 順列を辞書順にソート（itertools.permutations は既に辞書順で生成するが、念のため）
# permutations.sort() # 不要

a = -1
b = -1

for i, perm in enumerate(permutations):
    if perm == P:
        a = i
    if perm == Q:
        b = i
    if a != -1 and b != -1:
        break

print(abs(a - b))
