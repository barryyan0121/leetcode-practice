# @lc app=leetcode.cn id=1446 lang=python3


class Solution:
    def maxPower(self, s: str) -> int:
        best = current = 1
        for index in range(1, len(s)):
            current = current + 1 if s[index] == s[index - 1] else 1
            best = max(best, current)
        return best


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.maxPower, ("abbcccddddeeeeedcba",), 5)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1446 题 "连续字符" 所有测试用例通过')
