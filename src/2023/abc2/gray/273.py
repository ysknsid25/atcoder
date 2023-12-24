n=int(input())
a=list(map(int,input().split()))

a.sort()
aset=set(a)
count=[0]*n

for i in range(n):
    if a[i] in aset:
        aset.remove(a[i])
    count[len(aset)]+=1

for i in range(n):
    print(count[i])