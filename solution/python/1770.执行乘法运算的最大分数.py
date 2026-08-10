from functools import lru_cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        @lru_cache(None)
        def best(step: int, left: int) -> int:
            if step == m:
                return 0
            right = n - 1 - (step - left)
            multiplier = multipliers[step]
            return max(
                multiplier * nums[left] + best(step + 1, left + 1),
                multiplier * nums[right] + best(step + 1, left),
            )

        return best(0, 0)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumScore([1, 2, 3], [3, 2, 1]) == 14
    assert solution.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]) == 102
    print("1770 passed")
