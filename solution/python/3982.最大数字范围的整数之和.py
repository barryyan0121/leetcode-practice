"""3982. 最大数字范围的整数之和"""


class Solution:
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


if __name__ == "__main__":
    assert Solution().maxDigitRange([5724, 111, 350]) == 6074
    assert Solution().maxDigitRange([90, 900]) == 990
