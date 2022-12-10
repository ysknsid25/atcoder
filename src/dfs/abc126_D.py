n=int(input())
con=[[] for i in range(n)]
line=[[] for i in range(n)] for i in range(n)
for i in range(n):
  fr,to,w=,map(int,input().split())
  con[fr].append(to)
  con[to].append(fr)
  line[fr][to]=w
  line[to][fr]=w
