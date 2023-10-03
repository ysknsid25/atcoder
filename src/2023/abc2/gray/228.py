n,k=map(int,input().split())
score=[0]*n
scoreMap={}
for i in range(n):
    tmp=list(map(int,input().split()))
    score[i]=sum(tmp)

sortedScore=sorted(score,reverse=True)
rank={}
before=0
for i in range(n):
    before+=1
    if sortedScore[i] not in rank:
        rank[sortedScore[i]]=before

border=sortedScore[k-1]
for i in range(n):
    if (score[i]+300)>=border:
        print("Yes")
    else:
        print("No")