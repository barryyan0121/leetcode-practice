# @lc app=leetcode.cn id=1332 lang=python3


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        return 1 if s == s[::-1] else 2


if __name__ == "__main__":
    test_cases = [
        (Solution().removePalindromeSub, ("ababa",), 1),
        (Solution().removePalindromeSub, ("abb",), 2),
        (Solution().removePalindromeSub, ("",), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1332 题 "删除回文子序列" 所有测试用例通过')
