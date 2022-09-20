def intSort(a, isDesc):
  stra = str(a)
  lista = list(stra)
  lista.sort(reverse=isDesc)
  sortedstr = "".join(lista)
  return int(sortedstr)

def f(a):
  x = intSort(a, True)
  y = intSort(a, False)
  z = x - y
  return z

n, k = map(int, input().split())

a = n
for i in range(1, k+1):
  a = f(a)

print(a)