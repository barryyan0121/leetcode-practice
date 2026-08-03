# @lc app=leetcode.cn id=1396 lang=python3
from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.active = {}
        self.trips = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, begin = self.active.pop(id)
        record = self.trips[(start, stationName)]
        record[0] += t - begin
        record[1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.trips[(startStation, endStation)]
        return total / count


if __name__ == "__main__":
    test_cases = ["underground"]
    for _, _case in enumerate(test_cases):
        pass
    system = UndergroundSystem()
    system.checkIn(45, "Leyton", 3)
    system.checkOut(45, "Waterloo", 15)
    assert system.getAverageTime("Leyton", "Waterloo") == 12
    print('第 1396 题 "设计地铁系统" 所有测试用例通过')
