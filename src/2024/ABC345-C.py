from collections import defaultdict

s=list(input())
n=len(s)
total=(n*(n-1)/2)
a_set=set(s)

if len(a_set)==1:
  print(1)
  exit()

a_dict=defaultdict(int)
for c in s:
  a_dict[c]+=1

add = 0
for v in a_dict.values():
  if v > 1:
    # aaabb みたいな場合の入れ替え後の結果は1つとして数えるらしい
    # ありえるものを数えるので、免許証の問題っぽい
    add = 1 
  total -= (v*(v-1)/2) 

print(int(total)+add)