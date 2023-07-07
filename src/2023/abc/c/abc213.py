h,w,n=map(int,input().split())
row=set()
col=set()
raddis=[]

for i in range(n):
    r,c=map(int,input().split())
    row.add(r)
    col.add(c)
    raddis.append([r,c])

row=list(row)
col=list(col)

row.sort()
col.sort()

row_map={}
col_map={}

for i in range(len(row)):
    row_map[row[i]]=i+1

for i in range(len(col)):
    col_map[col[i]]=i+1

for i in range(n):
    print(row_map[raddis[i][0]],col_map[raddis[i][1]])