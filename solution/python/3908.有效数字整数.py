"""3908. 有效数字整数"""


class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        digits = str(n)
        target = str(x)
        return digits[0] != target and target in digits


if __name__ == "__main__":
    test_cases = [((101, 0), True), ((7, 7), False), ((123, 4), False)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().validDigit(*args) == expected
