n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list.sort()
b_list.sort()

i = 0
j = 0
ans = 10**15

while i < n and j < m:
    a = a_list[i]
    b = b_list[j]
    ans = min(ans, abs(a-b))
    if a > b:
        j += 1
    elif a < b:
        i += 1
    else:
        ans = 0
        break
print(ans)
