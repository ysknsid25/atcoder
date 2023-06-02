s,t,x=map(int,input().split())
fr=s
to=t
if t<s:
    to+=24
if x<s:
    x+=24
if fr<=x and x<to:
    print("Yes")
else:
    print("No")