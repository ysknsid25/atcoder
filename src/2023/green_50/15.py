n=int(input())
l=len(str(n))

nums=list(str(n))

one=0
two=0
zero=0
for str_num in nums:
    num=int(str_num)
    mod=num%3
    if mod == 0:
        zero+=1
    elif mod==1:
        one+=1
    else:
        two+=1

mod=n%3

if mod == 0:
    print(0)
elif mod == 1:
    if one > 0:
      if l <= 1:
        print(-1)
      else:
        print(1)
    else:
      if l <= 2:
        print(-1)
      else:
        print(2)
else:
    if two > 0:
      if l <= 1:
        print(-1)
      else:
          print(1)
    else:
      if l <= 2:
          print(-1)
      else:
          print(2)