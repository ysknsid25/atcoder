n,k=map(int,input().split())
a=list(map(int,input().split()))
sorta=a.copy()
sorta.sort()
dist=k//n
mod=k%n
mod_map={}
for i in range(mod):
    mod_map[sorta[i]]=True

for who in a:
    if who in mod_map:
        print(dist+1)
    else:
        print(dist)