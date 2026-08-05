"""2108. 找出数组中的第一个回文字符串"""


class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        return next((word for word in words if word == word[::-1]), "")


if __name__ == "__main__":
    test_cases = [((["abc", "car", "ada", "racecar", "cool"],), "ada")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().firstPalindrome(*args) == expected
