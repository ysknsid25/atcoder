
def judge(a,b):
  if a=="G" and b=="G":
    return 0,0
  elif a=="G" and b=="C":
    return 1,0
  elif a=="G" and b=="P":
    return 0,1
  elif a=="C" and b=="C":
    return 0,0
  elif a=="C" and b=="P":
    return 1,0
  elif a=="C" and b=="G":
    return 0,1
  elif a=="P" and b=="P":
    return 0,0
  elif a=="P" and b=="G":
    return 1,0
  elif a=="P" and b=="C":
    return 0,1

n,m=map(int, input().split())
te=[]
for i in range(2*n):
  tmp=list(input())
  te.append(tmp)

wins=[]
for i in range(n*2):
  wins.append([0,i])
  
for i in range(m):
  for k in range(n):
    pa=wins[2*k][1]
    pb=wins[2*k+1][1]

    ate=te[pa][i]
    bte=te[pb][i]

    ap,bp=judge(ate,bte)

    wins[2*k][0]-=ap
    wins[2*k+1][0]-=bp
  wins.sort()

for i in range(2*n):
  print(wins[i][1]+1)