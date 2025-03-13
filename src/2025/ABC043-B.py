s=list(input())
stack=[]
for c in s:
  if c=="B":
    if len(stack)>0:
      stack.pop()
  else:
    stack.append(c)
print("".join(stack))