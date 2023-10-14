n=int(input())
s=["1"]
for i in range(n):
    s.append(s[i]+" "+(str(int(i+2)))+" "+s[i])
print(s[n-1])
