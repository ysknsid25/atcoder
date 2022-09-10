import itertools
n, m = map(int, input().split())

s = []
for i in range(n):
  tmp = input()
  s.append(tmp)

t = []
for i in range(m):
  tmp = input()
  t.append(tmp)

c_list = list(itertools.permutations(s, n))
word = ""
for str_list in c_list:
  word = ""
  for tmp in str_list:
    if word == "":
      word += tmp
    else:
      word += "_" + tmp
  if len(word) >= 17 or len(word) < 3:
    word = ""
    break

  if word == "":
    continue

  isUnique = True
  for i in range(m):
    check = t[i]
    if word == check:
      wordUCnt = word.count("_")
      checkUCnt = check.count("_")
      if wordUCnt > 0 and wordUCnt == checkUCnt:
        idx = word.find("_")
        word = word[:idx] + '_' + word[idx:]
        if (len(word) > 16 or len(word) < 3):
          isUnique = False
          break
      elif wordUCnt == 0 and checkUCnt == 0:
          isUnique = False
          break

if word != "" and isUnique:
  print(word)
else:
  print(-1)