N = int(input())
res = 0
st = []
a=list(map(int,input().split()))

for num in a:
    if not st or st[-1][0] != num:
        st.append([num, 1])
        res += 1
    else:
        st[-1][1] += 1
        res += 1
        if st[-1][1] == st[-1][0]:
            res -= st[-1][0]
            st.pop()
    print(res)
    