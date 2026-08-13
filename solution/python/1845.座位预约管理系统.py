import heapq


class SeatManager:
    def __init__(self, n: int):
        self.available = list(range(1, n + 1))
        heapq.heapify(self.available)

    def reserve(self) -> int:
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)


if __name__ == "__main__":
    manager = SeatManager(3)
    assert [manager.reserve(), manager.reserve()] == [1, 2]
    manager.unreserve(1)
    assert manager.reserve() == 1
