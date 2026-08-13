from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total = sum(cost)
        keep = defaultdict(int)
        for ch, value in zip(s, cost):
            keep[ch] += value
        return total - max(keep.values())


if __name__ == "__main__":
    solution = Solution()
    assert solution.minCost("aabaac", [1, 2, 3, 4, 1, 10]) == 11
    assert solution.minCost("abc", [10, 5, 8]) == 13
    assert solution.minCost("zzzzz", [67, 67, 67, 67, 67]) == 0
