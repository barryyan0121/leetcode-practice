"""3498. 字符串的反转度"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i + 1) * (26 - (ord(char) - ord("a"))) for i, char in enumerate(s))


if __name__ == "__main__":
    test_cases = [
        (("abc",), 148),
        (("zaza",), 160),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().reverseDegree(s) == expected
