"""3627. 中位数之和的最大值"""


class Solution:
    def maximumMedianSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[len(nums) - 2 - 2 * i] for i in range(len(nums) // 3))


if __name__ == "__main__":
    test_cases = [([2, 1, 3, 2, 1, 3], 5), ([1, 1, 1], 1)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maximumMedianSum(nums) == expected
