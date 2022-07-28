n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnta = 0
cntb = 0
for i in range(n):
    inta = a[i]
    intb = b[i]
    cnttmp = b.count(inta)
    if inta == intb:
        cnta += 1
        if cnttmp > 0:
            cntb -= 1
    cntb += cnttmp

print(cnta)
print(cntb)
