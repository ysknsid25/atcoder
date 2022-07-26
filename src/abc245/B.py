N = int(input())
numarr = list(map(int, input().split()))

for i in range(0, N+1):
    result = i in numarr
    if not result:
        print(i)
        break
