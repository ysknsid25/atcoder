n=int(input())
l=[]
for i in range(n):
    a,c=map(int, input().split())
    l.append((a,c, i+1))
l.sort(key=lambda x: (-x[0], x[1]))

ans=[l[0][2]]
now=0
for i in range(1,n):
  if l[i][1] < l[now][1]:
    ans.append(l[i][2])
    now = i

ans.sort()
print(len(ans))
print(*ans)
