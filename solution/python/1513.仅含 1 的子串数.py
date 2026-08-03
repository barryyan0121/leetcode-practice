# @lc app=leetcode.cn id=1513 lang=python3


class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        result = current = 0
        for char in s:
            current = current + 1 if char == "1" else 0
            result = (result + current) % mod
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.numSub, ("0110111",), 9)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1513 题 "仅含 1 的子串数" 所有测试用例通过')
