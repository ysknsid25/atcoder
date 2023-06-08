n=int(input())
if n>=42:
    n+=1
# 0埋めで3桁表示
print("AGC" + str(n).zfill(3))