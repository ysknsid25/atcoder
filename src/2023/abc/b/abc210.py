n=int(input())
s=list(input())
for i in range(n):
    isBad = s[i]=="1"
    if isBad and i%2==0:
        print("Takahashi")
        exit()
    elif isBad:
        print("Aoki")
        exit()