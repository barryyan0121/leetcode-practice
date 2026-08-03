# @lc app=leetcode.cn id=2102 lang=python3

import heapq


class _Best:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score
        return self.name < other.name


class _Worst:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name


class SORTracker:
    def __init__(self):
        self.remaining = []
        self.selected = []

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.remaining, _Best(name, score))
        if self.selected and self.remaining[0].__lt__(
            _Best(self.selected[0].name, self.selected[0].score)
        ):
            best = heapq.heappop(self.remaining)
            worst = heapq.heappop(self.selected)
            heapq.heappush(self.remaining, _Best(worst.name, worst.score))
            heapq.heappush(self.selected, _Worst(best.name, best.score))

    def get(self) -> str:
        best = heapq.heappop(self.remaining)
        heapq.heappush(self.selected, _Worst(best.name, best.score))
        return best.name


if __name__ == "__main__":

    def run_operations(operations):
        tracker = SORTracker()
        result = []
        for operation, args in operations:
            value = getattr(tracker, operation)(*args)
            if operation == "get":
                result.append(value)
        return result

    test_cases = [
        (
            run_operations,
            (
                [
                    ("add", ("brad", 2)),
                    ("add", ("bran", 3)),
                    ("get", ()),
                    ("add", ("alexa", 2)),
                    ("get", ()),
                    ("add", ("aron", 2)),
                    ("get", ()),
                ],
            ),
            ["bran", "alexa", "aron"],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2102 题 "序列顺序查询" 所有测试用例通过')
