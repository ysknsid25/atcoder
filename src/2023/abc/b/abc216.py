n=int(input())
names = {}
for i in range(n):
    s,t=input().split()
    name=s+" "+t
    if name in names:
        print("Yes")
        exit()
    else:
        names[name]=name
print("No")