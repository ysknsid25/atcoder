def sum_of_absolute_differences(A):
    A.sort()  # 昇順ソート
    N = len(A)
    total = 0
    for i in range(N):
        total += A[i] * (2 * i - (N - 1))
    return total


n=int(input())
a=list(map(int, input().split()))
result = sum_of_absolute_differences(a)
print(result)
