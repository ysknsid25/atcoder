stry = input().split()
y = int(stry[0])
mod = y % 4

if mod < 2:
    print(y + (2 - mod))
elif mod == 2:
    print(y)
else:
    print(y+mod)
