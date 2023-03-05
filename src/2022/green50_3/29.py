# ans = 全体-(0を含まない+9を含まない-0,9両方含まない)
n = int(input())

# 一つは絶対0で、それ以外の桁を9以外のから選ぶの
all = 10**n
zero = 9**n
nine = 9**n
zeronine = 8**n
ans = all-(zero+nine-zeronine)
ans %= (10**9+7)
print(ans)