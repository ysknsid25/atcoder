def bigger(a, b):
    lena = len(str(a))
    lenb = len(str(b))
    if lena > lenb:
        return lena
    else:
        return lenb


n = int(input())
i = 1
ans = 10**15
while i*i <= n:
    if n % i == 0:
        a = n//i
        b = i
        res = bigger(a, b)
        ans = min(ans, res)
    i += 1
print(ans)
