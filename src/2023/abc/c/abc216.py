n=int(input())
ans=[]
while n>0:
    if n%2==1:
        ans.append("A")
        n-=1
    else:
        ans.append("B")
        n//=2
ans.reverse()
print("".join(ans))