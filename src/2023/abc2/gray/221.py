n=list(input())
ans=-10**40

# 探索範囲は、nが3桁であれば
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# の順にbitは変わっていく
for bit in range(1<<len(n)):
    a=[]
    b=[]
    for shift in range(len(n)):
        if (bit >> shift) & 1:
            a.append(n[shift])
        else:
            b.append(n[shift])
    if len(a)==0 or len(b)==0:
        continue
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans=max(int("".join(a))*int("".join(b)), ans)
print(ans)