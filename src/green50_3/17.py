n = int(input())

nums = set()
for a in range(2, 10**6):
  for b in range(2, 34):
    if a**b > n:
      break
    else:
      nums.add(a**b)

ans = n - len(nums)
print(ans)