s = input()
arr = list(s)
sum = 0
for i in range(0, len(s)):
    sum += int(s[i])

result = 45 - sum
print(result)
