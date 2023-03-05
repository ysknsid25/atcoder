import itertools

n = int(input())
c = list(map(int, input().split()))
clen = len(c)

pairs = []
for pair in itertools.permutations(c, clen):
    pairs.append(pair)

total = len(pairs)

if total < 2:
    ans = total % 100003
    print(ans)
    exit()

for pair in pairs:
    for i in range(2, clen):
        back2 = pair[i-2]
        back1 = pair[i-1]
        now = pair[i]
        if back1 > now and back2 > now:
            total -= 1
ans = total % 100003
print(ans)
