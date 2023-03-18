n,k=map(int,input().split())
p=list(map(int,input().split()))

exp=[]
for num in p:
    e=(num+1)/2
    exp.append(e)

ans=0
for i in range(k):
    ans+=exp[i]

before=ans
for i in range(1,n-k+1):
    tmp=before-exp[i-1]+exp[i-1+k]
    before=tmp
    ans=max(ans, before)

print(ans)