class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        index = 0
        while index < len(s) and index < len(t) and s[index] == t[index]:
            index += 1
        if index == len(s) or index == len(t):
            return min(len(s), len(t))
        index += 1
        while index < len(s) and index - 1 < len(t) and s[index] == t[index - 1]:
            index += 1
        return index - 1


if __name__ == "__main__":
    test_cases = [
        (("madxa", "madam"), 4),
        (("leetcode", "eetcode"), 7),
        (("one", "one"), 3),
        (("a", "b"), 0),
        (("abc", "ab"), 2),
    ]
    for _, ((s, t), expected) in enumerate(test_cases):
        assert Solution().longestCommonPrefix(s, t) == expected
