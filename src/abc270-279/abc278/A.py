n,k = map(int, input().split())
a = list(map(str,input().split()))

for i in range(k):
  a.append("0")

res = a[k:]
ans = " ".join(res)
print(ans)