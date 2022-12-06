x=int(input())
p=x
ans=x
while True:
  i=2
  isPrime=True
  while i*i<=p:
    if p%i==0:
      isPrime=False
      break
    i+=1
  if isPrime:
    ans=p
    break
  p+=1
print(ans)