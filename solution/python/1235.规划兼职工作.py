from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        ends, best = [], [0]
        for start, end, value in sorted(
            zip(startTime, endTime, profit), key=lambda x: x[1]
        ):
            best.append(max(best[-1], value + best[bisect_right(ends, start)]))
            ends.append(end)
        return best[-1]


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]), 120),
        (([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]), 150),
    ]
    for _, ((start, end, profit), expected) in enumerate(test_cases):
        assert Solution().jobScheduling(start, end, profit) == expected
