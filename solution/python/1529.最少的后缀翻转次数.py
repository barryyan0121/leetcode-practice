# @lc app=leetcode.cn id=1529 lang=python3


class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        state = "0"
        for char in target:
            if char != state:
                flips += 1
                state = char
        return flips


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.minFlips, ("10111",), 3)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1529 题 "最少的后缀翻转次数" 所有测试用例通过')
