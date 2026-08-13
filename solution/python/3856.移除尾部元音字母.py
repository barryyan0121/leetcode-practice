"""3856. 移除尾部元音字母"""


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip("aeiou")


if __name__ == "__main__":
    test_cases = [(("idea",), "id"), (("day",), "day"), (("aeiou",), "")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().trimTrailingVowels(*args) == expected
