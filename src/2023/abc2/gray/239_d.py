a,b,c,d = map(int, input().split())

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

isTakahashiWin=False
for x in range(a, b+1):
    hasPrime=False
    for y in range(c, d+1):
        n=x+y
        if isPrime(n):
          hasPrime=True
          break
    if not hasPrime:
      isTakahashiWin=True
if isTakahashiWin:
  print("Takahashi")
else:
  print("Aoki")