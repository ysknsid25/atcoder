n,k=map(int,input().split())
plist=[]
psort=[]
for i in range(n):
  tmp=list(map(int,input().split()))
  score=sum(tmp)
  plist.append(score)
  psort.append(score)

psort.sort(reverse=True)
minscore = psort[k-1]
for score in plist:
  if (score+300) >= minscore:
    print("Yes")
  else:
    print("No")