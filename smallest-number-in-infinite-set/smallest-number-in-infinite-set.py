from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.curMax = 0
        self.ss = SortedSet()
        self.ss.add(1)
    def popSmallest(self) -> int:
        num = self.ss.pop(0)
        self.curMax = max(self.curMax, num)
        if len(self.ss) == 0 :
            self.ss.add(self.curMax + 1)
        return num

    def addBack(self, num: int) -> None:
        if num  <= self.curMax :
            self.ss.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)