n=int(input())
a=list(map(int,input().split()))

def calcor(l,r,a):
  res=0
  for i in range(l,r):
    res|=a[i]
  return res

ans=10**20
for i in range(1<<(n+1)):
  #右端もしくは左端が0になっているものは飛ばす
  #001 100 000 のような3パターン
  #端がないと全ての数を区切れないため
  if i&1==0 or i>>n&1==0:
    continue
  p=[]
  for shift in range(n+1):
    #! shift桁目を確認し、1であれば仕切りがあるので桁を追加
    if i>>shift&1==1:
      p.append(shift)

  tmp=0
  for j in range(len(p)-1):
    #区間ごとの計算結果をXOR
    tmp^=calcor(p[j],p[j+1],a)
  ans=min(ans,tmp)

print(ans)