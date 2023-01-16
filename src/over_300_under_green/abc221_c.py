n=input()
ans=0

for bit in range(1<<len(n)):
  a=[]
  b=[]
  for shift in range(len(n)):
    if bit >> shift & 1 == 0:
      a.append(n[shift])
    else:
      b.append(n[shift])

  if a==[] or b==[]:
    continue
  a.sort(reverse=True)
  b.sort(reverse=True)

  a_join="".join(a)
  b_join="".join(b)

  tmp = int(a_join)*int(b_join)
  ans=max(tmp,ans)

print(ans)