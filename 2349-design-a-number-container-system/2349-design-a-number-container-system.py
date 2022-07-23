from heapq import heapify, heappush, heappop

class NumberContainers:
    def __init__(self):

        self.dic = {}
        
        self.indexDic = {}
    def change(self, index: int, number: int) -> None:
        
        self.indexDic[index] = number
        if number in self.dic:
            heappush(self.dic[number],index)
        else:
            heap = []
            heapify(heap)
            # s.add(index)
            heappush(heap,index)
            self.dic[number] = heap
    def find(self, number: int) -> int:
        # print(self.arr)
        if number not  in self.dic :
            # print(self.dic,self.i)
            # self.i +=1
            return -1
        
        while len(self.dic[number]) > 0:
            
            idx = self.dic[number][0]
            if self.indexDic[idx] == number:
                return idx
            heapq.heappop(self.dic[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)