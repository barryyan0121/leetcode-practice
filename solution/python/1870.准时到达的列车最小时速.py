from math import ceil
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        left, right = 1, 10**7
        while left < right:
            speed = (left + right) // 2
            time = sum(ceil(value / speed) for value in dist[:-1]) + dist[-1] / speed
            if time <= hour:
                right = speed
            else:
                left = speed + 1
        return left


if __name__ == "__main__":
    solver = Solution()
    assert solver.minSpeedOnTime([1, 3, 2], 6) == 1
    assert solver.minSpeedOnTime([1, 3, 2], 2.7) == 3
