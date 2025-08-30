Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())
S = [input().split() for _ in range(M)]
T = [input().split() for _ in range(L)]

move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

s_moves = []
for char, length in S:
  s_moves.append((move[char], int(length)))

t_moves = []
for char, length in T:
  t_moves.append((move[char], int(length)))

R_diff = Ra - Rt
C_diff = Ca - Ct

ans = 0
s_idx, t_idx = 0, 0
s_rem, t_rem = s_moves[0][1], t_moves[0][1]

while s_idx < M and t_idx < L:
  step = min(s_rem, t_rem)

  s_dr, s_dc = s_moves[s_idx][0]
  t_dr, t_dc = t_moves[t_idx][0]
  dR = t_dr - s_dr
  dC = t_dc - s_dc

  if dR == 0 and dC == 0:
      if R_diff == 0 and C_diff == 0:
          ans += step
  elif dR == 0:
      if R_diff == 0 and dC != 0 and -C_diff % dC == 0:
          s = -C_diff // dC
          if 1 <= s <= step:
              ans += 1
  elif dC == 0:
      if C_diff == 0 and dR != 0 and -R_diff % dR == 0:
          s = -R_diff // dR
          if 1 <= s <= step:
              ans += 1
  else: # dR != 0 and dC != 0
      if -R_diff % dR == 0 and -C_diff % dC == 0:
          s_r = -R_diff // dR
          s_c = -C_diff // dC
          if s_r == s_c and 1 <= s_r <= step:
              ans += 1

  R_diff += step * dR
  C_diff += step * dC

  s_rem -= step
  t_rem -= step

  if s_rem == 0:
      s_idx += 1
      if s_idx < M:
          s_rem = s_moves[s_idx][1]
  
  if t_rem == 0:
      t_idx += 1
      if t_idx < L:
          t_rem = t_moves[t_idx][1]

print(ans)
