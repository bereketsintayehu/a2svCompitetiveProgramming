from statistics import mean
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.stations = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t1 = self.customer[id]
        self.stations[startStation + '->' + stationName].append(t -t1)
        del self.customer[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.stations[startStation + '->' + endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)