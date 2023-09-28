from collections import defaultdict
n,m=map(int, input().split())
d=defaultdict(int)
for i in range(2*n):
    d[i]=0
a=[]
for i in range(n*2):
    a.append(list(input()))

for i in range(m):
    d = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))
    l = list(d)
    for me in range(0,n*2-1,2):
        you=me+1
        if a[l[me]][i]==a[l[you]][i]:
            continue
        elif a[l[me]][i]=="G" and a[l[you]][i]=="C":
            d[l[me]]+=1
        elif a[l[me]][i]=="C" and a[l[you]][i]=="P":
            d[l[me]]+=1
        elif a[l[me]][i]=="P" and a[l[you]][i]=="G":
            d[l[me]]+=1
        else:
            d[l[you]]+=1
d = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))
for key in d:
    print(key+1)