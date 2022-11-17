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

n=int(input())
prms = list(set(prime_factorize(n)))
ans = 0
for p in prms:
  e=1
  if p==1:
    continue
  while p**e <= n:
    z = p**e
    if n%z == 0:
      n//=z
      ans += 1
    e+=1

print(ans)