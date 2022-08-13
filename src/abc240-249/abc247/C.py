n = int(input())

outstr = ""
bkout = ""
for i in range(1, (n+1)):
    out = i
    if i == 1:
        outstr = str(i)
        bkout = outstr
    else:
        outstr = str(bkout) + ' ' + str(out) + ' ' + str(bkout)
        bkout = outstr

print(outstr)
