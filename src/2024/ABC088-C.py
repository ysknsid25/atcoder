c=[list(map(int, input().split())) for _ in range(3)]

for a1 in range(0, 101):
  for a2 in range(0, 101):
    for a3 in range(0, 101):
      b00 = c[0][0] - a1
      b01 = c[0][1] - a1
      b02 = c[0][2] - a1
      b10 = c[1][0] - a2
      b11 = c[1][1] - a2
      b12 = c[1][2] - a2
      b20 = c[2][0] - a3
      b21 = c[2][1] - a3
      b22 = c[2][2] - a3
      if (b00 == b10 == b20) and (b01 == b11 == b21) and (b02 == b12 == b22):
        print("Yes")
        exit()
print("No")