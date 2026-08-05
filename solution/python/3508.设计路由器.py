from bisect import bisect_left, bisect_right
from collections import defaultdict, deque


class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packets = deque()
        self.present = set()
        self.times = defaultdict(list)
        self.removed = defaultdict(int)

    def _remove(self) -> list[int]:
        packet = list(self.packets.popleft())
        self.present.remove(tuple(packet))
        self.removed[packet[1]] += 1
        return packet

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.present:
            return False
        if len(self.packets) == self.memory_limit:
            self._remove()
        self.packets.append(packet)
        self.present.add(packet)
        self.times[destination].append(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        return self._remove() if self.packets else []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        values = self.times[destination]
        left = self.removed[destination]
        return bisect_right(values, endTime, left) - bisect_left(
            values, startTime, left
        )


if __name__ == "__main__":
    test_cases = [3]
    for _, memory_limit in enumerate(test_cases):
        router = Router(memory_limit)
        assert router.addPacket(1, 4, 90)
        assert router.addPacket(2, 5, 90)
        assert not router.addPacket(1, 4, 90)
        assert router.addPacket(3, 5, 95)
        assert router.addPacket(4, 5, 105)
        assert router.forwardPacket() == [2, 5, 90]
        assert router.addPacket(5, 2, 110)
        assert router.getCount(5, 100, 110) == 1
