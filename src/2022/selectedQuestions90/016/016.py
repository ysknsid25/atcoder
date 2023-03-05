n = int(input())
a,b,c= map(int,input().split())

L = 9999
num = L
for i in range(0, L):
  L2 = L - i
  for j in range(0, L2):
    k = (n - a*i - b*j) // c
    if a*i + b*j + c*k == n and k >= 0:
        num = min(num, i+j+k)

print(num)