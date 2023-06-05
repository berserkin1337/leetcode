class FrequencyTracker:

    def __init__(self):
        self.hasFreqTracker  = defaultdict(set)
        self.dicc =  defaultdict(int)


    def add(self, number: int) -> None:
        freq = self.dicc[number]
        if freq != 0 :
            self.hasFreqTracker[freq].remove(number)
            if len(self.hasFreqTracker[freq])  == 0 :
                del self.hasFreqTracker[freq]
        
        self.dicc[number] += 1
        self.hasFreqTracker[self.dicc[number]].add(number)

    def deleteOne(self, number: int) -> None:
        if number not in self.dicc :
            return 
        freq = self.dicc[number]
        if freq != 0 :
            self.hasFreqTracker[freq].remove(number)
            if len(self.hasFreqTracker[freq])  == 0 :
                del self.hasFreqTracker[freq]
        self.dicc[number] -= 1
        if self.dicc[number] != 0 :
            self.hasFreqTracker[self.dicc[number]].add(number)
        else:
            del self.dicc[number]

    def hasFrequency(self, frequency: int) -> bool:
        # print(self.hasFreqTracker)
        if frequency in self.hasFreqTracker :
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)