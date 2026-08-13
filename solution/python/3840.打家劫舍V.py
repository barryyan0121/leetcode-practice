from typing import List


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        previous_two = 0
        previous = 0
        for i, value in enumerate(nums):
            current = max(
                previous,
                value
                + (previous if i and colors[i] != colors[i - 1] else previous_two),
            )
            previous_two, previous = previous, current
        return previous


if __name__ == "__main__":
    assert Solution().rob([1, 4, 3, 5], [1, 1, 2, 2]) == 9
    assert Solution().rob([3, 1, 2, 4], [2, 3, 2, 2]) == 8
