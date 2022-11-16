n=int(input())
i=1
ans = 0
while i*i <= 2*n:
  if 2*n%i==0:
    x = i
    y = 2*n//i
    if x%2!=y%2:
      ans += 2
  i+=1
print(ans)