"""2160. 拆分数位后四位数字的最小和"""


class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        return int(digits[0] + digits[2]) + int(digits[1] + digits[3])


if __name__ == "__main__":
    test_cases = [((2932,), 52)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumSum(*args) == expected
