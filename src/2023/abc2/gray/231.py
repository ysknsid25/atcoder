n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

for i in range(q):
    x=int(input())
    if x < a[0]:
        print(n)
        continue
    elif a[n-1] < x:
        print(0)
        continue
    left = 0
    right = n-1
    while 1 < right - left:
        now = (left + right) // 2
        if a[now] < x:
            left = now
        else:
            right = now
    print(n-right)
