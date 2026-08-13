"""3227. 字符串中的元音游戏"""


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(char in "aeiou" for char in s)


if __name__ == "__main__":
    test_cases = [
        ("leetcoder", True),
        ("bbb", False),
    ]
    for index, (s, expected) in enumerate(test_cases):
        assert Solution().doesAliceWin(s) == expected, index
