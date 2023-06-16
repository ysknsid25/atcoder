types={'ABC':0,'ARC':0,'AGC':0,'AHC':0}

s1=input()
s2=input()
s3=input()
s=[s1,s2,s3]

for i in range(3):
    if s[i]=="ABC":
        types['ABC']+=1
    elif s[i]=="ARC":
        types['ARC']+=1
    elif s[i]=="AGC":
        types['AGC']+=1
    elif s[i]=="AHC":
        types['AHC']+=1

for k,v in types.items():
    if v==0:
        print(k)
        exit()