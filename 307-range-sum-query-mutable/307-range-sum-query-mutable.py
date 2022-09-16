class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.t = [0]*(4*self.n)
        self._build(nums,1,0,self.n-1)
    def _build(self,a,v,tl,tr):
        if tl == tr:
            self.t[v] = a[tl]
            return
        tm = (tl+tr)//2
        self._build(a,v*2,tl,tm)
        self._build(a,v*2+1,tm+1,tr)
        self.t[v] = self.t[v*2] + self.t[v*2 +1]
    def update(self, index: int, val: int) -> None:
        self._update(1,0,self.n-1,index,val)

    def _update(self,v,tl,tr,pos,new_val):
        if tl == tr :
            self.t[v] = new_val
            return
        tm = (tl+tr) // 2
        if pos <= tm :
            self._update(v*2,tl,tm,pos,new_val)
        else:
            self._update(v*2+1,tm+1,tr,pos,new_val)
        self.t[v] = self.t[v*2] + self.t[v*2 +1]
        
        
    def sumRange(self, left: int, right: int) -> int:
        return self._sum(1,0,self.n  - 1,left,right)
        
    def _sum(self,v,tl,tr,l,r):
        if l > r :
            return 0
        if l == tl and r == tr :
            return self.t[v]
        tm =( tl + tr ) // 2
        return self._sum(v*2, tl, tm, l, min(r, tm)) + self._sum(v*2+1, tm+1, tr, max(l, tm+1), r)

        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)