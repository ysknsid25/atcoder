s=list(input())
isWeak = False
sl=set(s)
if len(sl)==1:
    print("Weak")
    exit()

for i in range(3):
    now=int(s[i])
    nxt=int(s[i+1])
    if (now==9 and nxt==0) or (now+1==nxt):
        isWeak = True
        continue
    else:
        isWeak=False
        break

if isWeak:
    print("Weak")
else:
    print("Strong")