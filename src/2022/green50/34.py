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
if n == 1:
  print(0)
  exit()

primaries = prime_factorize(n)
setPrimaries = set(primaries)
cnt = 0
num = n
e = 1
for p in setPrimaries:
  iscontinue = True
  while iscontinue:
    z = p ** e
    if num % z == 0:
      cnt += 1
      num = num // z
      e += 1
    else:
      iscontinue = False
      e = 1

print(cnt)