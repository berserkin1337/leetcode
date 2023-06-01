class UndergroundSystem:
    # value: (start_time , start_station ), key : id
    # key (start_station,end_station) , value : (totalTime, totalTrips)
    def __init__(self):
        self.checkedIn = {}
        self.totalTimes = {}    

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (t,stationName)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime,startStation = self.checkedIn[id]
        totalTime ,  totalTrips = 0,0  
        if (startStation,stationName) in self.totalTimes :
            totalTime , totalTrips = self.totalTimes[( (startStation,stationName))]
        totalTime += (t - startTime)
        totalTrips += 1
        self.totalTimes[( (startStation,stationName))] = (totalTime , totalTrips)
        
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime ,  totalTrips = self.totalTimes[(startStation,endStation)]
        return totalTime/totalTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)