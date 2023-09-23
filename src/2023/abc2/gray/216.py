n=int(input())
ans=0
if n==1:
    print("A")
    exit()
if n==2:
    print("AA")
    exit()

ans=[]
while n>2:
    if n%2==0:
        n=n//2
        ans.append("B")
    else:
        n=n-1
        ans.append("A")
ans.append("A")
ans.append("A")
ans.reverse()
print("".join(ans))