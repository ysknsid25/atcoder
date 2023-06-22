s=list(input())
ans=0

for num in range(10000):
    strnum=str(num)
    strnum=strnum.zfill(4)
    isValid=True
    for i in range(10):
        if s[i]=="o" and str(i) not in strnum:
            isValid=False
            break
        if s[i]=="x" and str(i) in strnum:
            isValid=False
            break
    if isValid:
        ans+=1
print(ans)