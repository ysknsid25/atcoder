n,q = map(int, input().split())
fmap = {}

for i in range(q):
  t,a,b = map(int, input().split())
  if t==1:
    if a in fmap:
      fr = fmap[a]
      fr[b] = True
      fmap[a] = fr
    else:
      fr = {}
      fr[b] = True
      fmap[a] = fr
  elif t==2:
    if a in fmap:
      fr = fmap[a]
      fr[b] = False
      fmap[a] = fr
    else:
      fr = {}
      fr[b] = False
      fmap[a] = fr
  else:
    isAFollowB = False
    isBFollowA = False
    if a in fmap:
      fr = fmap[a]
      if b in fr:
        isAFollowB = fr[b]
    if b in fmap:
      fr = fmap[b]
      if a in fr:
        isBFollowA = fr[a]
    if isAFollowB and isBFollowA:
      print("Yes")
    else:
      print("No")