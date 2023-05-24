import copy
h,w,k=map(int,input().split())
c=[]
for i in range(h):
    tmp=list(input())
    c.append(tmp)

ph=2**h
pw=2**w

ans=0
for hbit in range(ph):
    for wbit in range(pw):
        r=copy.deepcopy(c)
        for i in range(h):
            if (hbit >> i) & 1:
                tmp=['' for x in range(w)]
                r[i]=tmp
            for j in range(w):
                if (wbit >> j) & 1:
                    for l in range(h):
                        r[l][j]=""
        cnt=0
        for i in range(h):
            for j in range(w):
                char=r[i][j]
                if char=='#':
                    cnt+=1
        if cnt==k:
            ans+=1
print(ans)