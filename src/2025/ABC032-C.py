n,k = map(int, input().split())
s=[int(input()) for _ in range(n)]

for num in s:
  if num == 0:
    print(n)
    exit()

right=0
ans=0
res=1
for left in range(n):
  # ここが部分列の条件
  while right<n and res*s[right]<=k:
    res*=s[right]
    right+=1
  ans=max(right-left, ans)
  if left==right:
    right+=1
  else:
    res//=s[left]
print(ans)