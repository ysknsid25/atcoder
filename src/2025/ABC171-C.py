n=int(input())
result = ""
while n > 0:
    n -= 1  # 1-indexed に対応するために調整
    result = chr(ord('a') + (n % 26)) + result
    n //= 26
print(result)
