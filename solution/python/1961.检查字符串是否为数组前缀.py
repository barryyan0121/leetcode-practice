"""1961. 检查字符串是否为数组前缀"""


class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word
            if prefix == s:
                return True
            if len(prefix) > len(s):
                return False
        return False


if __name__ == "__main__":
    test_cases = [
        (("iloveleetcode", ["i", "love", "leetcode"]), True),
        (("iloveleetcode", ["apples", "i", "love", "leetcode"]), False),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isPrefixString(*args) == expected
