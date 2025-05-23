n,m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
begin = 0
if n > 1:
  begin = 10**(n-1)
end = 10**n
for i in range(begin, end):
    str_num = str(i)
    find = True
    for s,c in sc:
        if str_num[s-1] != str(c):
            find = False
            break
    if find:
        print(i)
        exit()
print(-1)