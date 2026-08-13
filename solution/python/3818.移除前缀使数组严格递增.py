from typing import List


class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                return i + 1
        return 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumPrefixLength([1, 2, 3]) == 0
    assert solution.minimumPrefixLength([1, 1, 2, 3]) == 1
