k=int(input())
kbit=bin(k)
ans=kbit.replace("1", "2")
print(ans[2:])
