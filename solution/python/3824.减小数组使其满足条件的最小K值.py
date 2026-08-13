from typing import List


class Solution:
    def minimumK(self, nums: List[int]) -> int:
        left, right = 1, max(len(nums), max(nums))
        while left < right:
            k = (left + right) // 2
            if sum((value + k - 1) // k for value in nums) <= k * k:
                right = k
            else:
                left = k + 1
        return left


if __name__ == "__main__":
    assert Solution().minimumK([1, 2, 3]) == 2
