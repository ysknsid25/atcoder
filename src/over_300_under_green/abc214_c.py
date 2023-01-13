n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
time = [10**15]*n

for i in range(n):
    nxt = (i+1) % n
    #! 高橋くんから貰うのが早いのか、隣の人から貰うのが早いのか
    time[nxt] = min(t[nxt], time[i]+s[i])

for i in range(n-1):
    nxt = (i+1) % n
    #! １番目に貰うタイミングが極端に遅い場合は、となりのすぬけ君から貰う方が早い場合があるのでその考慮
    #! 1周目で計算した時間の方が早いのか、隣のすぬけ君から貰うのが早いのか
    time[nxt] = min(time[i]+s[i], time[nxt])

for ans in time:
    print(ans)
