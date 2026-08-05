"""2119. 数字经过双倍反转后的结果"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0


if __name__ == "__main__":
    test_cases = [((526,), True), ((1800,), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isSameAfterReversals(*args) == expected
