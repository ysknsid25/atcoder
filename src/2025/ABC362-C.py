n = int(input())
L = []
R = []
sum_L = 0
sum_R = 0

for _ in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    sum_L += l
    sum_R += r

if 0 < sum_L or sum_R < 0:
    print("No")
else:
    print("Yes")

remain = sum_L
result = L[:]

for i in range(n):
    d = min(R[i] - L[i], -remain)
    result[i] += d
    remain += d

print(" ".join(map(str, result)))
