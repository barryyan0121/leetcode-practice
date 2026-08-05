"""2165. 重排数字的最小值"""


class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = num < 0
        digits = sorted(str(abs(num)), reverse=negative)
        if not negative and digits[0] == "0":
            first = next(index for index, digit in enumerate(digits) if digit != "0")
            digits[0], digits[first] = digits[first], digits[0]
        value = int("".join(digits))
        return -value if negative else value


if __name__ == "__main__":
    test_cases = [((310,), 103), ((-7605,), -7650)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().smallestNumber(*args) == expected
