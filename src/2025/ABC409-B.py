def max_x(N, A):
    def is_ok(x):
        count = sum(1 for a in A if a >= x)
        return count >= x

    left, right = 0, max(A) + 1
    while right - left > 1:
        mid = (left + right) // 2
        if is_ok(mid):
            left = mid
        else:
            right = mid
    return left

N = int(input())
A = list(map(int, input().split()))
print(max_x(N, A))
