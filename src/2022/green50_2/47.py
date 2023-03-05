#! セグメントツリー
"""
演算を行う。必要に応じて変更する
"""
def segfunc(x,y):
    return x^y

class SegTree:
    def __init__(self,x_list,init,segfunc):
        self.init=init
        self.segfunc=segfunc
        self.Height=len(x_list).bit_length()+1
        self.Tree=[init]*(2**self.Height)
        self.num=2**(self.Height-1)
        for i in range(len(x_list)):
            self.Tree[2**(self.Height-1)+i]=x_list[i]
        for i in range(2**(self.Height-1)-1,0,-1):
            self.Tree[i]=segfunc(self.Tree[2*i],self.Tree[2*i+1])

        """指定のインデックスの値を返す
        """
    def select(self,k):
        return self.Tree[k+self.num]

        """指定のインデックスの値を更新する
        """
    def update(self,k,x):
        i=k+self.num
        self.Tree[i]=x
        while i>1:
            if i%2==0:
                self.Tree[i//2]=self.segfunc(self.Tree[i],self.Tree[i+1])
            else:
                self.Tree[i//2]=self.segfunc(self.Tree[i-1],self.Tree[i])
            i//=2

        """指定区間についての演算結果を返す
        """
    def query(self,l,r):
        result=self.init
        l+=self.num
        r+=self.num+1

        while l<r:
            if l%2==1:
                result=self.segfunc(result,self.Tree[l])
                l+=1
            if r%2==1:
                result=self.segfunc(result,self.Tree[r-1])
            l//=2
            r//=2
        return result

n,q=map(int,input().split())
a=list(map(int,input().split()))
sg=SegTree(a,0,segfunc)
for i in range(q):
  t,x,y=map(int,input().split())
  x-=1
  if t==1:
    sg.update(x,segfunc(sg.select(x),y))
  else:
    y-=1
    print(sg.query(x,y))