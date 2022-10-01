n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0

if n <= 2 and a[0] != 1:
  print(0)
  exit()

if n <= 2 and a[0] == 1:
  print(1)
  exit()

want = 0
cnt = 0
beforecnt = cnt
changeindex = n-1
for i in range(n):
  kan = a[i] - 1
  if kan != want:
    if changeindex > 1:
      changeindex -= 2
    else:
      break
  want += 1
  cnt += 1
  if beforecnt >= cnt:
    cnt -= 1
    break
  if cnt == (n-1):
    break
print(cnt)