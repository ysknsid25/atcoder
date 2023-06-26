a,b,c=map(int,input().split())
isAPlus=a>=0
isBPlus=b>=0
isCEven=c%2==0

if (isAPlus and not isBPlus and isCEven) or (not isAPlus and isBPlus and isCEven):
    a=abs(a)
    b=abs(b)

if a==b:
    print("=")
elif a>b:
    print(">")
else:
    print("<")