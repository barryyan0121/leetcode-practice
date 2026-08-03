# @lc app=leetcode.cn id=1400 lang=python3
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and sum(count % 2 for count in Counter(s).values()) <= k


if __name__ == "__main__":
    test_cases = [
        (Solution().canConstruct, ("annabelle", 2), True),
        (Solution().canConstruct, ("leetcode", 3), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1400 题 "构造 K 个回文字符串" 所有测试用例通过')
