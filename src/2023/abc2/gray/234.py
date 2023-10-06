k=int(input())
hist=[]
mod=k
hist.append(mod)
while mod > 1:
    mod=mod//2
    hist.append(mod)
hist.sort()

ans=2
for num in hist:
    if num==1:
        continue
    if num%2==1:
        ans=ans*10+2
    else:
        ans=ans*10
print(ans)