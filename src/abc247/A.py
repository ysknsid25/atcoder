s = input()
arr = list(s.rstrip('\n'))

result = "0"
for i in range(1, len(arr)):
    if arr[i-1] == "1":
        result = result + "1"
    else:
        result = result + "0"

print(result)
