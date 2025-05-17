a, b, c, d = map(int, input().split())

# 締切時刻を分単位に変換
deadline = a * 60 + b

# 提出時刻を分単位に変換
submission = c * 60 + d

# 締切前に提出しているか判定
if submission <= deadline:
    print("Yes")
else:
    print("No")