p=list(map(int,input().split()))
s=[chr(i) for i in range(97,97+26)]
ans=[]
for i in range(26):
    ans.append(s[p[i]-1])
print("".join(ans))