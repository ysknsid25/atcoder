import itertools
s,k=map(str,input().split())
s_list=list(s)
k=int(k)

ans=set()
p = itertools.permutations(s_list, len(s_list))
for v in p:
    new_s=''.join(v)
    ans.add(new_s)

ans=list(ans)
ans.sort()
print(ans[k-1])