n=int(input())
full_time=0
doukasen=[]
for i in range(n):
    a,b=map(int, input().split())
    doukasen.append([a,b])
    full_time+=a/b
time=full_time/2
dist=0
for a,b in doukasen:
    if time>=a/b:
        time-=a/b
        dist+=a
    else:
        dist+=time*b
        break
print(dist)

