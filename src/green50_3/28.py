h,w,k = map(int,input().split())
r = []
for i in range(h):
  c = list(input())
  r.append(c)

hp = 2**h
wp = 2**w
ans = 0
for hb in range(hp):
  for wb in range(wp):
    blkcnt = 0
    for row in range(h):
      if (hb >> row) & 1:
        continue
      else:
        rtmp = r[row]
        for col in range(w):
          if (wb >> col) & 1:
            continue
          else:
            string = rtmp[col]
            if string == "#":
              blkcnt += 1
    if k==blkcnt:
      ans += 1

print(ans)

