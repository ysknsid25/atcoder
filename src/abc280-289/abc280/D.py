k=int(input())
num = 1
for n in range(2,10000):
  num *= n
  if num%k==0:
    print(n)
    exit()

print(k)