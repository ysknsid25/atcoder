n = int(input())

adanaseiarr = []
adanameiarr = []
result = "Yes"
for i in range(n):
    s, t = input().split()
    adanaseiarr.append(s)
    adanameiarr.append(t)

for i in range(n):
    sei = adanaseiarr[i]
    mei = adanameiarr[i]
    isExistSei = False
    isExistMei = False
    for j in range(n):
        if i == j:
            continue
        isExistSei = isExistSei or sei == adanaseiarr[j] or sei == adanameiarr[j]
        isExistMei = isExistMei or mei == adanameiarr[j] or mei == adanaseiarr[j]
    if isExistSei and isExistMei:
        print("No")
        exit()

print("Yes")
