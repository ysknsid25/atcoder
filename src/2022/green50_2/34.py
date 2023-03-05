def prime_factorize(N):
    if N==1:
        return [1]
    prime_list=[]
    i=2
    while i*i<=N:
        if N%i==0:
            prime_list.append(i)
            N//=i
        else:
            i+=1
    if N!=1:
        prime_list.append(N)
    return prime_list

n = int(input())
primenumbers = prime_factorize(n)
primenumbers = set(primenumbers)
found = {}
ans = 0
isContinue = True
e = 1
while isContinue:
  isContinue = False
  for p in primenumbers:
    if p == 1:
      continue
    z = p**e
    if z in found:
      continue
    else:
      if n%z == 0:
        isContinue = True
        found[z] = 1
        ans += 1
        n /= z
  e += 1
print(ans)