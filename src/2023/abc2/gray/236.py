n,m=map(int,input().split())
s=list(map(str,input().split()))
t=list(map(str,input().split()))
express={}
for station in t:
    express[station]=1

for station in s:
    if station in express:
        print("Yes")
    else:
        print("No")