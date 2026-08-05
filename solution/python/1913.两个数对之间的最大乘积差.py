"""1913. 两个数对之间的最大乘积差"""


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        ordered = sorted(nums)
        return ordered[-1] * ordered[-2] - ordered[0] * ordered[1]


if __name__ == "__main__":
    test_cases = [([5, 6, 2, 7, 4], 34), ([4, 2, 5, 9, 7, 4, 8], 64)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maxProductDifference(nums) == expected
