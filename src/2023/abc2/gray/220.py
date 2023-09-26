n=int(input())
a=list(map(int, input().split()))
x=int(input())
div=sum(a)
d=x//div
mod=x%div
for i in range(n):
    mod-=a[i]
    if mod<0:
        print((d*n)+i+1)
        exit()