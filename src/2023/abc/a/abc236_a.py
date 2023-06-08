s=list(input())
a,b=map(int,input().split())
sa=s[a-1]
sb=s[b-1]
s[a-1]=sb
s[b-1]=sa
print("".join(s))