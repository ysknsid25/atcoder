
r, c = map(int, input().split())
r -= 1
c -= 1

arr = [["b","b","b","b","b","b","b","b","b","b","b","b","b","b","b"],
["b","w","w","w","w","w","w","w","w","w","w","w","w","w","b"],
["b","w","b","b","b","b","b","b","b","b","b","b","b","w","b"],
["b","w","b","w","w","w","w","w","w","w","w","w","b","w","b"],
["b","w","b","w","b","b","b","b","b","b","b","w","b","w","b"],
["b","w","b","w","b","w","w","w","w","w","b","w","b","w","b"],
["b","w","b","w","b","w","b","b","b","w","b","w","b","w","b"],
["b","w","b","w","b","w","b","w","b","w","b","w","b","w","b"],
["b","w","b","w","b","w","b","b","b","w","b","w","b","w","b"],
["b","w","b","w","b","w","w","w","w","w","b","w","b","w","b"],
["b","w","b","w","b","b","b","b","b","b","b","w","b","w","b"],
["b","w","b","w","w","w","w","w","w","w","w","w","b","w","b"],
["b","w","b","b","b","b","b","b","b","b","b","b","b","w","b"],
["b","w","w","w","w","w","w","w","w","w","w","w","w","w","b"],
["b","b","b","b","b","b","b","b","b","b","b","b","b","b","b"]]

color = arr[r][c]

if color == "b":
  print("black")
else:
  print("white")