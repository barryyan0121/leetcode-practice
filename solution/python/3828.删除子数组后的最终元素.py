from typing import List


class Solution:
    def finalElement(self, nums: List[int]) -> int:
        return max(nums[0], nums[-1])


if __name__ == "__main__":
    assert Solution().finalElement([1, 3, 2]) == 2
