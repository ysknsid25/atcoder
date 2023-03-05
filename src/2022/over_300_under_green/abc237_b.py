n=int(input())
seq=set()
for i in range(n):
  tmp=list(map(int,input().split()))
  tmp=tuple(tmp)
  seq.add(tmp)
print(len(seq))