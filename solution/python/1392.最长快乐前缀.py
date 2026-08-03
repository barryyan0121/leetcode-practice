# @lc app=leetcode.cn id=1392 lang=python3
class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix = [0] * len(s)
        matched = 0
        for index in range(1, len(s)):
            while matched and s[index] != s[matched]:
                matched = prefix[matched - 1]
            if s[index] == s[matched]:
                matched += 1
            prefix[index] = matched
        return s[: prefix[-1]] if s else ""


if __name__ == "__main__":
    test_cases = [
        (Solution().longestPrefix, ("level",), "l"),
        (Solution().longestPrefix, ("ababab",), "abab"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1392 题 "最长快乐前缀" 所有测试用例通过')
