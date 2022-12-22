k = int(input())
mod = 7 % k
if mod == 0:
    print(1)
    exit()

for i in range(2, k+1):
    mod = (mod*10+7) % k
    if mod == 0:
        print(i)
        exit()

print(-1)
