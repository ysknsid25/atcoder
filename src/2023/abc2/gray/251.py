n=int(input())
mvp={}
ans=-1
mvp_score=0
mvp_index=-1
for i in range(n):
    s,t=map(str,input().split())
    if s not in mvp:
        mvp[s]=int(t)
        if mvp_score<int(t):
            mvp_index=i
            mvp_score=int(t)
print(mvp_index+1)