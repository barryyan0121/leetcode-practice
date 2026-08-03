# @lc app=leetcode.cn id=1573 lang=python3


class Solution:
    def numWays(self, s: str) -> int:
        mod = 10**9 + 7
        ones = s.count("1")
        if ones == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % mod
        if ones % 3:
            return 0
        part = ones // 3
        first = second = 0
        seen = 0
        for char in s:
            if char == "1":
                seen += 1
            elif seen == part:
                first += 1
            elif seen == 2 * part:
                second += 1
        return (first + 1) * (second + 1) % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numWays, ("10101",), 4), (solution.numWays, ("1001",), 0)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1573 题 "分割字符串的方案数" 所有测试用例通过')
