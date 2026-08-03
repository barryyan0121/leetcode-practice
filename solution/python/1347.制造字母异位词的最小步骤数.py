# @lc app=leetcode.cn id=1347 lang=python3

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())


if __name__ == "__main__":
    test_cases = [
        (Solution().minSteps, ("bab", "aba"), 1),
        (Solution().minSteps, ("leetcode", "practice"), 5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1347 题 "制造字母异位词的最小步骤数" 所有测试用例通过')
