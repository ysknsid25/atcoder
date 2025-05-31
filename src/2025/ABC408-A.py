n,s=map(int, input().split())
t=list(map(int, input().split()))

th=0
time=0
last=0
for i in range(n):
  th=last+s+0.5
  if t[i] > th:
    print("No")
    exit()
  last=t[i]
print("Yes")
