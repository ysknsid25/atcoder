a=list(input())
b=list(input())
found = False
cnt = 0
for i in range(len(a)):
  ca = a[i]
  cb = b[i]
  if not ca == cb:
    cnt = i+1
    found = True
    break

if not found:
  cnt = len(b)

print(cnt)