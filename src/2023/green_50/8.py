def g(s, isReverse=True):
  tmp=list(s)
  tmp.sort(reverse=isReverse)
  strNum = "".join(tmp)
  return int(strNum)

n,k=map(int,input().split())
s=str(n)

a=s
for i in range(k):
  num = g(a) - g(a, False)
  a=str(num)

print(a)