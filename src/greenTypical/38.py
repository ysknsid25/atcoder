n,x=map(int,input().split())
s=list(input())
move=[]
for c in s:
  if len(move)==0:
    move.append(c)
  else:
    #! 位置が変わらないパターン
    if c=="U" and (move[-1]=="L" or move[-1]=="R"):
      move.pop()
    elif c=="L" or c=="R":
      move.append(c)
    elif c=="U" or move[-1]=="U":
      move.append(c)

now=x
for c in move:
  if c=="U":
    now//=2
  elif c=="L":
    now*=2
  else:
    now*=2
    now+=1
print(now)