"""3099. 哈沙德数"""


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = sum(map(int, str(x)))
        return digit_sum if x % digit_sum == 0 else -1


if __name__ == "__main__":
    test_cases = [(18, 9), (23, -1)]
    for _, (x, expected) in enumerate(test_cases):
        assert Solution().sumOfTheDigitsOfHarshadNumber(x) == expected
