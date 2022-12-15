k=int(input())
before=0
for i in range(k):
  n=before*10+7
  before=n%k
  if before==0:
    print(i+1)
    exit()
print(-1)