from collections import defaultdict

s = list(input())
d = defaultdict(int)
last = defaultdict(int)
stack = []

for i in range(len(s)):
    c = s[i]
    if d[c] == 1:
        print("No")
        exit()
        
    if c == '(':
        stack.append(i)
    elif c == ')':
        back = stack.pop()
        # lastでループを回して、valueがback以上i未満のdを0にする
        for k, v in last.items():
            if back <= v < i:
                d[k] = 0
    else:
        d[c] = 1
        last[c] = i
print("Yes")