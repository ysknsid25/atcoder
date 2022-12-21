from math import gcd

n=int(input())
a=list(map(int,input().split()))

#! 素数因数についてAの最大値まであらかじめ計算しておく
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

#! 素因数を返す
def fast_prime_fact(primes,num):
  prime=[]
  while 1<num:
    prime.append(primes[num])
    num//=primes[num]
  return prime

is_used=[False for i in range(10**6+7)]
is_pairwise=True
for num in a:
  res=fast_prime_fact(primes,num)
  res=set(res)
  for p in res:
    if is_used[p]:
      is_pairwise=False
      break
    else:
      is_used[p]=True

if is_pairwise:
  print("pairwise coprime")
  exit()

g=a[0]
for nxt in a:
  g=gcd(g,nxt)

if g==1:
  print("setwise coprime")
else:
  print("not coprime")