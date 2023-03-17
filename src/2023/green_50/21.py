a,b,w=map(int,input().split())

ans_max=-10**9
ans_min=10**9

for x in range(1, 10**6+1):
    if (a*x) <= (1000*w) <= (b*x):
        ans_max=max(ans_max, x)
        ans_min=min(ans_min, x)

if ans_max==-10**9 or ans_min==10**9:
    print("UNSATISFIABLE")
else:
    print(ans_min, ans_max)