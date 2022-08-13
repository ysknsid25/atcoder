a, b, k = map(int, input().split())

ret = a
cnt = 1
while ret < b:
    ret = ret * k
    cnt += 1

# 最後の1回を引く
total = cnt - 1
print(total)