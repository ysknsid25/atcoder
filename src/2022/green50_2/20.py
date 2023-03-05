n = int(input())
s = input()
q = int(input())

s = "0" + s
s = list(s)
flip = False

for i in range(q):
  t,a,b = map(int, input().split())
  if t == 1:
    if flip:
      if a <= n:
        a += n
      else:
        a -= n
      if b <= n:
        b += n
      else:
        b -= n
    s[a], s[b] = s[b], s[a]
  else:
    flip = not flip

left = s[1:n+1]
right= s[n+1:]

if flip:
  ans = right + left
else:
  ans = left + right

print("".join(ans))