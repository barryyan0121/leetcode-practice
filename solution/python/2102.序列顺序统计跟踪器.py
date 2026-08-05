"""2102. 序列顺序统计跟踪器"""

import heapq


class SORTracker:
    def __init__(self):
        self.rest = []
        self.top = []
        self.count = 0

    @staticmethod
    def best_key(name: str, score: int):
        return (-score, tuple(ord(char) for char in name), name)

    @staticmethod
    def worst_key(name: str, score: int):
        return (score, tuple(-ord(char) for char in name), name)

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.rest, (self.best_key(name, score), name, score))
        if self.top and self.rest[0][0] < self.top[0][0]:
            worst = heapq.heappop(self.top)
            best = heapq.heappop(self.rest)
            heapq.heappush(
                self.rest, (self.best_key(worst[2], worst[1]), worst[2], worst[1])
            )
            heapq.heappush(
                self.top, (self.worst_key(best[1], best[2]), best[1], best[2])
            )

    def get(self) -> str:
        self.count += 1
        best = heapq.heappop(self.rest)
        heapq.heappush(self.top, (self.worst_key(best[1], best[2]), best[1], best[2]))
        worst = self.top[0]
        return worst[1]


if __name__ == "__main__":
    test_cases = [(1, "bradford", 2)]
    for _, (score, name, expected) in enumerate(test_cases):
        tracker = SORTracker()
        tracker.add(name, score)
        assert tracker.get() == name
