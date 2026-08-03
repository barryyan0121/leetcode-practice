# @lc app=leetcode.cn id=1688 lang=python3


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numberOfMatches, (7,), 6),
        (solution.numberOfMatches, (14,), 13),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1688 题 "比赛中的配对次数" 所有测试用例通过')
