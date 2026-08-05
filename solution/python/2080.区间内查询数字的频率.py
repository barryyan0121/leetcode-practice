"""2080. 区间内查询数字的频率"""

from bisect import bisect_left, bisect_right
from collections import defaultdict


class RangeFreqQuery:
    def __init__(self, arr: list[int]):
        self.positions = defaultdict(list)
        for index, value in enumerate(arr):
            self.positions[value].append(index)

    def query(self, left: int, right: int, value: int) -> int:
        positions = self.positions[value]
        return bisect_right(positions, right) - bisect_left(positions, left)


if __name__ == "__main__":
    test_cases = [(([1, 1, 2, 1], 0, 2, 1), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert RangeFreqQuery(args[0]).query(*args[1:]) == expected
