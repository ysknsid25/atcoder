s,t=map(str,input().split())
s=list(s)
t=list(t)
l=min(len(s),len(t))
for i in range(l):
    cs=ord(s[i])
    ct=ord(t[i])
    if cs>ct:
        print("Yes")
        exit()
    elif cs<ct:
        print("No")
        exit()