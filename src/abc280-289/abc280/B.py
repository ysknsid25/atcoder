n=int(input())
s=list(map(int,input().split()))
s.reverse()
res = []
for i in range(n-1):
  tmp = s[i] - s[i+1]
  strnum = str(tmp)
  res.append(strnum)
res.append(str(s[n-1]))
res.reverse()
ans = " ".join(res)
print(ans)