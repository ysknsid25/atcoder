s1=input()
s2=input()
s3=input()
s=[s1,s2,s3]
t=list(input())
ans=[]
for i in range(len(t)):
    ans.append(s[int(t[i])-1])
print("".join(ans))