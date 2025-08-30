def f(x):
    return int(str(x)[::-1])

X, Y = map(int, input().split())

a_prev = X
a_curr = Y

for _ in range(8):
    a_next = f(a_prev + a_curr)
    a_prev = a_curr
    a_curr = a_next

print(a_curr)
