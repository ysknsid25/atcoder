n,k=map(str, input().split())

def g(s, isReverse=True):
    tmp=list(s)
    tmp.sort(reverse=isReverse)
    strNum = "".join(tmp)
    return int(strNum)

k=int(k)
for i in range(k):
    num = g(n) - g(n, False)
    n=str(num)

print(n)