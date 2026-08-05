"""1967. 作为子字符串出现在单词中的字符串数目"""


class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        return sum(pattern in word for pattern in patterns)


if __name__ == "__main__":
    test_cases = [((["a", "abc", "bc", "d"], "abc"), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numOfStrings(*args) == expected
