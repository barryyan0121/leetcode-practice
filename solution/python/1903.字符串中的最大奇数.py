"""1903. 字符串中的最大奇数"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for index in range(len(num) - 1, -1, -1):
            if int(num[index]) % 2:
                return num[: index + 1]
        return ""


if __name__ == "__main__":
    test_cases = [("52", "5"), ("4206", "")]
    for _, (num, expected) in enumerate(test_cases):
        assert Solution().largestOddNumber(num) == expected
