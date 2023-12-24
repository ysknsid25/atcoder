n=int(input())
a=list(map(int,input().split()))

odd=[]
even=[]

for num in a:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

odd.sort(reverse=True)
even.sort(reverse=True)

if len(odd) > 1 or len(even)>1:
    sum_odd=0
    sum_even=0
    if len(odd)>1:
        sum_odd=odd[0]+odd[1]
    if len(even)>1:
        sum_even=even[0]+even[1]
    print(max(sum_odd,sum_even))
else:
    print(-1)