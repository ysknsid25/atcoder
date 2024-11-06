n = int(input())
q = int(input())
box = [[] for i in range(0, n+1)]
numbers = [set() for i in range(0, 2*10**5+1)]
for i in range(q):
    list = input().split()
    query = list[0]
    if query == '1':
        i = int(list[1])
        j = int(list[2])
        box[j].append(i)
        numbers[i].add(j)
    elif query == '2':
        i = int(list[1])
        print(' '.join(map(str, sorted(box[i]))))
    else:
        j = int(list[1])
        print(' '.join(map(str, sorted(numbers[j]))))
