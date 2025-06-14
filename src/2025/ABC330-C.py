import math


def min_abs_diff(D: int) -> int:
    max_val = int(math.isqrt(2 * D)) + 1
    min_diff = abs(D)
    for x in range(max_val + 1):
        x2 = x * x
        # y^2 = D - x^2 付近を二分探索
        left, right = 0, max_val
        while left <= right:
            mid = (left + right) // 2
            y2 = mid * mid
            total = x2 + y2
            diff = abs(total - D)
            if diff < min_diff:
                min_diff = diff
                if min_diff == 0:
                    return 0
            if total < D:
                left = mid + 1
            else:
                right = mid - 1
        # 近傍も確認（midの前後）
        for y in [right, left]:
            if 0 <= y <= max_val:
                y2 = y * y
                total = x2 + y2
                diff = abs(total - D)
                if diff < min_diff:
                    min_diff = diff
                    if min_diff == 0:
                        return 0
    return min_diff

D=int(input())
result = min_abs_diff(D)
print(result)