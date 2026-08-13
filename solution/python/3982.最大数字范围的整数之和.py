#
# @lc app=leetcode.cn id=3982 lang=python3
#
# [3982] 最大数字范围的整数之和
#


class Solution:
    # @lc code=start
    def maxDigitRange(self, nums: list[int]) -> int:
        ranges = []
        for number in nums:
            digits = [int(digit) for digit in str(number)]
            ranges.append(max(digits) - min(digits))
        maximum = max(ranges)
        return sum(
            number
            for number, digit_range in zip(nums, ranges)
            if digit_range == maximum
        )

    # @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([5724, 111, 350],), 6074),
        (([90, 900],), 990),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxDigitRange(*args) == expected
