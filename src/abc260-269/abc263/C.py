import itertools

n, m = list(map(int, input().split()))
numarr = [str(x) for x in range(1, (m+1))]

for c in itertools.combinations(numarr, n):
    out = ' '.join(c)
    print(out)
