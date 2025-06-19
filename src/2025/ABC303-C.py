dict_x={}
dict_y={}

n,m,h,k=map(int, input().split())
s=list(input())
p=[]

for i in range(m):
    x,y=map(int, input().split())
    if x not in dict_x:
        dict_x[x] = {}
    if y not in dict_x[x]:
        dict_x[x][y] = True

dict_command = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

move=0
x,y= 0, 0
for c in s:
    h-=1
    if h<0:
        break
    dx, dy = dict_command[c]
    x += dx
    y += dy
    move += 1
    if x in dict_x and y in dict_x[x] and dict_x[x][y] and h < k:
        h = k
        dict_x[x][y] = False

if move == n:
    print("Yes")
else:
    print("No")
