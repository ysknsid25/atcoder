a=list(input())
b=list(input())

if a==b:
    print("Yes")
    exit()

for i in range(len(a)-1):
    a[i],a[i+1]=a[i+1],a[i]
    if a==b:
        print("Yes")
        exit()
    a[i],a[i+1]=a[i+1],a[i]

print("No")