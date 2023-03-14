n=int(input())
nums=set()

i=2
while i**2 <= n:
    k=2
    num=i
    while num**k <= n:
        nums.add(num**k)
        k+=1
    i+=1

nums=list(nums)
ans=n-len(nums)
print(ans)