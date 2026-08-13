"""2349. 设计数字容器系统"""

import heapq


class NumberContainers:
    def __init__(self):
        self.values = {}
        self.indices = {}

    def change(self, index: int, number: int) -> None:
        self.values[index] = number
        heap = self.indices.setdefault(number, [])
        heapq.heappush(heap, index)

    def find(self, number: int) -> int:
        heap = self.indices.get(number, [])
        while heap and self.values.get(heap[0]) != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1


if __name__ == "__main__":
    system = NumberContainers()
    system.change(2, 10)
    system.change(1, 10)
    assert system.find(10) == 1
