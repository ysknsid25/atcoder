"""
heapqを使って解く問題。
heapqの計算量は、
・リストをheap化する(NlogN)
・最小値を参照する(1)
・要素を追加、削除する(logN)
最小値しか参照できないが、値を負の数で格納することで
最大値を取り出すことが可能となる。
"""
import heapq

n,m=map(int,input().split())
a=list(map(int,input().split()))
a_minus = []
for i in range(n):
    a_minus.append(-1*a[i])

#! リストをheap化
heapq.heapify(a_minus)
for i in range(m):
    #! ヒープからリストの最小値を取り出し、同時に取り出した要素をリストから削除できる
    x=heapq.heappop(a_minus)
    
    # クーポンの適用
    x/=2
    x=int(x)
    
    #! ヒープに値を追加する
    heapq.heappush(a_minus,x)

ans = -1 * sum(a_minus)
print(ans)