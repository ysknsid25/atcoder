n,k=map(int,input().split())

arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])

arr.sort()
x=k
for i in range(n):
    a,b=arr[i]
    if x<a:
      break
    else:
      x+=b

print(x)