amap = {"a": [2,4,7,8], "b":[3,6,9,10]}
bmap = {"a": [6,10], "b":[2,4,5,7,8]}
cmap = {"a": [10], "b":[2,3,4,5,7,8,9]}
dmap = {"a": [4,7], "b":[2,5,6,9,10]}
emap = {"a": [7], "b":[2,3,5,6,8,9,10]}

def judge2(arr, pins):
  for i in range(len(arr)):
    index = arr[i] - 1
    if pins[index] == "1":
      return True
  return False

def judge(arr1, arr2, pins):
  a = judge2(arr1, pins)
  b = judge2(arr2, pins)
  return a and b

pins = list(input())

if pins[0] == "1":
  print("No")
  exit()

result = True 
if pins[0] == "0" and pins[4] == "0":
  result = judge(amap["a"], amap["b"], pins)
elif pins[2] == "0" and pins[8] == "0":
  result = judge(bmap["a"], bmap["b"], pins)
elif pins[5] == "0":
  result = judge(cmap["a"], cmap["b"], pins)
elif pins[1] == "0" and pins[7] == "0":
  result = judge(dmap["a"], dmap["b"], pins)
elif pins[3] == "0":
  result = judge(emap["a"], emap["b"], pins)
else:
  result = False

if result:
  print("Yes")
else:
  print("No")