from collections import Counter, deque
import heapq


class StatisticsTracker:
    def __init__(self):
        self.queue = deque()
        self.low = []
        self.high = []
        self.low_size = 0
        self.high_size = 0
        self.removed = set()
        self.side = {}
        self.next_id = 0
        self.counts = Counter()
        self.mode_heap = []
        self.total = 0

    def _clean_low(self) -> None:
        while self.low and self.low[0][1] in self.removed:
            heapq.heappop(self.low)

    def _clean_high(self) -> None:
        while self.high and self.high[0][1] in self.removed:
            heapq.heappop(self.high)

    def _rebalance(self) -> None:
        target_low = len(self.queue) // 2
        self._clean_low()
        self._clean_high()
        while self.low_size > target_low:
            self._clean_low()
            neg_number, item_id = heapq.heappop(self.low)
            heapq.heappush(self.high, (-neg_number, item_id))
            self.side[item_id] = 1
            self.low_size -= 1
            self.high_size += 1
        while self.low_size < target_low:
            self._clean_high()
            number, item_id = heapq.heappop(self.high)
            heapq.heappush(self.low, (-number, item_id))
            self.side[item_id] = 0
            self.low_size += 1
            self.high_size -= 1

    def addNumber(self, number: int) -> None:
        item_id = self.next_id
        self.next_id += 1
        self.queue.append((number, item_id))
        self._clean_low()
        self._clean_high()
        if not self.high or number < self.high[0][0]:
            heapq.heappush(self.low, (-number, item_id))
            self.side[item_id] = 0
            self.low_size += 1
        else:
            heapq.heappush(self.high, (number, item_id))
            self.side[item_id] = 1
            self.high_size += 1
        self.counts[number] += 1
        heapq.heappush(self.mode_heap, (-self.counts[number], number))
        self.total += number
        self._rebalance()

    def removeFirstAddedNumber(self) -> None:
        number, item_id = self.queue.popleft()
        self._clean_low()
        self._clean_high()
        self.removed.add(item_id)
        if self.side.pop(item_id) == 0:
            self.low_size -= 1
        else:
            self.high_size -= 1
        self.counts[number] -= 1
        self.total -= number
        self._rebalance()

    def getMean(self) -> int:
        return self.total // len(self.queue)

    def getMedian(self) -> int:
        self._clean_high()
        return self.high[0][0]

    def getMode(self) -> int:
        while self.mode_heap and -self.mode_heap[0][0] != self.counts[self.mode_heap[0][1]]:
            heapq.heappop(self.mode_heap)
        return self.mode_heap[0][1]


if __name__ == "__main__":
    test_cases = [
        ([4, 4, 2, 3], (3, 4, 4, 2)),
    ]
    for _, (numbers, expected) in enumerate(test_cases):
        tracker = StatisticsTracker()
        for number in numbers:
            tracker.addNumber(number)
        assert (tracker.getMean(), tracker.getMedian(), tracker.getMode()) == expected[:3]
        tracker.removeFirstAddedNumber()
        assert tracker.getMode() == expected[3]
