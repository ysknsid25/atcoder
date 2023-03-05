"""
鳩の巣原理
鳩の巣がN個、鳩がN+1羽いれば鳩が二匹以上いる巣が必ず一つはある
"""

k=int(input())
amari = 0
for i in range(1,k+1):
  amari = amari*10+7
  if amari%k==0:
    print(i)
    exit()
  amari%=k
print(-1)
  