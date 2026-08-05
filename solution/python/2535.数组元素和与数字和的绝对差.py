"""2535. 数组元素和与数字和的绝对差"""


class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        return abs(
            sum(nums) - sum(int(digit) for value in nums for digit in str(value))
        )


if __name__ == "__main__":
    test_cases = [(([1, 15, 6, 3],), 9)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().differenceOfSum(*args) == expected
