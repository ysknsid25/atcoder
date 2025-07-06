# setの計算量が1番大きく、それぞれO(N), O(M)であるため、O(N+M)となる。
# ソートはO(NlogN), 積集合はO(min(N,M))
def solution(arr1, arr2):
    return sorted(list(set(arr1) & set(arr2)))
