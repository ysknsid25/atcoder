class UnionFind:
  def __init__(self, n):
    self.n = n
    self.parent_size=[-1] * n

  """
  リーダーが同じなら何もしない
  リーダーが違う場合、グループの人数が少ない方を、大きい方のグループへ統合する
  """
  def merge(self, a, b):
    x, y = self.leader(a), self.leader(b)
    if x == y:
      return
    if abs(self.parent_size[x]) < abs(self.parent_size[y]):
      x, y = y, x
    self.parent_size[x] += self.parent_size[y]
    self.parent_size[y] = x
    return
  
  def same(self, a, b):
    return self.leader[a] == self.leader[b]

  """
  再帰で根にいるリーダーを探しに行く
  自分自身がリーダーなら自分を返す
  """
  def leader(self, a):
    if self.parent_size[a] < 0:
      return a
    self.parent_size[a] = self.leader(self.parent_size[a])
    return self.parent_size[a]

  """
  aが所属するグループのサイズ(人数)を返す
  """
  def size(self, a):
    return abs(self.parent_size[self.leader(a)])

  def groups(self):
    result = [[] for _ in range(self.n)]
    for i in range(self.n):
      result[self.leader(i)].append(i)
    return [r for r in result if r != []]

n,m = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
  a,b = map(int, input().split())
  a-=1
  b-=1
  uf.merge(a,b)

ans = 1
for i in range(0,n):
  grsize = uf.size(i)
  ans = max(ans, grsize)
print(ans)