from collections import deque
from typing import List


class RideSharingSystem:
    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.active = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.active.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] not in self.active:
            self.riders.popleft()
        if not self.riders or not self.drivers:
            return [-1, -1]
        rider = self.riders.popleft()
        self.active.remove(rider)
        return [self.drivers.popleft(), rider]

    def cancelRider(self, riderId: int) -> None:
        self.active.discard(riderId)


if __name__ == "__main__":
    system = RideSharingSystem()
    system.addRider(3)
    system.addDriver(2)
    assert system.matchDriverWithRider() == [2, 3]
