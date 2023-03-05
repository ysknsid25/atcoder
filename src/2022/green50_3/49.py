from math import gcd

n=int(input())
a_list=list(map(int,input().split()))
primes=[0 for i in range(10**6+7)]
for i in range(2,10**6+7):
  if primes[i]!=0:
    continue
  for j in range(10**6+7):
    if i*j<10**6+7:
      if primes[i*j]==0:
        primes[i*j]=i
    else:
      break

def fast_prime(primes,num):
  res=[]
  while num>1:
    res.append(primes[num])
    num//=primes[num]
  return res

is_primes=[False for i in range(10**6+7)]
is_prime=True
for a in a_list:
  res=fast_prime(primes,a)
  res=set(res)
  for num in res:
    if is_primes[num]:
      is_prime=False
      break
    else:
      is_primes[num]=True

if is_prime:
  print("pairwise coprime")
else:
  g=a_list[0]
  for i in range(1,n):
    g=gcd(g,a_list[i])
  if g==1:
    print("setwise coprime")
  else:
    print("not coprime")