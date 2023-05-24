n=int(input())
mod=10**9+7

a_all=pow(10,n,mod)
a_0=pow(9,n,mod)
a_9=pow(9,n,mod)
a_0_9=pow(8,n,mod)

ans=a_all-(a_0+a_9-a_0_9)
ans%=mod
print(ans)