s=input()
af=0
for i in range(len(s)):
    if s[i] == 'a':
        af+=1
    else:
        break

ab=0
for i in range(len(s)-1,-1,-1):
    if s[i] == 'a':
        ab+=1
    else:
        break

if ab < af:
    print("No")
    exit()

s = "a"*(ab-af) + s

n=len(s)
for i in range(n):
    if s[i] != s[n-i-1]:
        print("No")
        exit()

print("Yes")