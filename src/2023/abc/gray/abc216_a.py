s=input()
# 文字列を.で分割してリストに格納
a=s.split(".")
y=int(a[1])
if y<=2:
    print(a[0]+"-")
elif y<=6:
    print(a[0])
else:
    print(a[0]+"+")