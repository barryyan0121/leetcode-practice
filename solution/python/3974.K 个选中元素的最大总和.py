#
# @lc app=leetcode.cn id=3974 lang=python3
#
# [3974] K 个选中元素的最大总和
#


class Solution:
    # @lc code=start
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        selected = sorted(nums, reverse=True)[:k]
        weights = [max(mul - index, 1) for index in range(k)]
        return sum(value * weight for value, weight in zip(selected, weights))

    # @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([6, 1, 2, 9], 3, 2), 26),
        (([3, 7, 5, 2], 2, 4), 43),
        (([4, 4], 1, 1), 4),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxSum(*args) == expected
