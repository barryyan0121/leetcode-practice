# @lc app=leetcode.cn id=1672 lang=python3


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(map(sum, accounts))


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maximumWealth, ([[1, 2, 3], [3, 2, 1]],), 6),
        (solution.maximumWealth, ([[1, 5], [7, 3], [3, 5]],), 10),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1672 题 "最富有客户的资产总量" 所有测试用例通过')
