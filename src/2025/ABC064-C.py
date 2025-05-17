n=int(input())
s=list(map(int, input().split()))

colors=[0 for _ in range(8)]
blacks=0

for rate in s:
  if rate >= 3200:
    blacks += 1
  elif rate >= 2800:
    colors[7] += 1
  elif rate >= 2400:
    colors[6] += 1
  elif rate >= 2000:
    colors[5] += 1
  elif rate >= 1600:
    colors[4] += 1
  elif rate >= 1200:
    colors[3] += 1
  elif rate >= 800:
    colors[2] += 1
  elif rate >= 400:
    colors[1] += 1
  else:
    colors[0] += 1

color_count = 0
for i in range(8):
  if colors[i] > 0:
    color_count += 1

min_color = max(1, color_count)  # 最低1色は選べるようにする
max_color = color_count + blacks if color_count > 0 else min(blacks, 8)
print(f"{min_color} {max_color}")
