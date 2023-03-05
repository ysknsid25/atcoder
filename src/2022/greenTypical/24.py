def convert(before):
  tmp=set(before)
  tmp=list(tmp)
  tmp.sort()
  res={}
  for i in range(len(tmp)):
    res[tmp[i]]=i+1
  return res

h,w,n=map(int,input().split())
cards=[]
row=[]
col=[]

for i in range(n):
  a,b=map(int,input().split())
  cards.append([a,b])
  row.append(a)
  col.append(b)

row_convert=convert(row)
col_convert=convert(col)

for row_i, col_i in cards:
  print(row_convert[row_i],col_convert[col_i])