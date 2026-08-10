"""2221. 数组的三角和"""


class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) > 1:
            nums = [(a + b) % 10 for a, b in zip(nums, nums[1:])]
        return nums[0]
