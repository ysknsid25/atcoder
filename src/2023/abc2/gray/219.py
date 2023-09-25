x=list(input())
indexMap = {}
for i in range(len(x)):
    indexMap[x[i]]=i
alphas = list("abcdefghijklmnopqrstuvwxyz")
n=int(input())
converted=[]
originals={}
for i in range(n):
    key=input()
    s=list(key)
    for j in range(len(s)):
        s[j]=alphas[indexMap[s[j]]]
    converted.append("".join(s))
    originals["".join(s)]=key
converted.sort()
for i in range(n):
    print(originals[converted[i]])
    
