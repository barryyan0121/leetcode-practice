"""2332. 坐上公交的最晚时间"""


class Solution:
    def latestTimeCatchTheBus(
        self, buses: list[int], passengers: list[int], capacity: int
    ) -> int:
        buses.sort()
        passengers.sort()
        occupied = set(passengers)
        index = 0
        last = 0
        for bus in buses:
            count = 0
            while (
                index < len(passengers)
                and passengers[index] <= bus
                and count < capacity
            ):
                last = passengers[index]
                index += 1
                count += 1
        candidate = bus if count < capacity else last
        while candidate in occupied:
            candidate -= 1
        return candidate
