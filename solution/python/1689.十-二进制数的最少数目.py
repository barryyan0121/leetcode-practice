# @lc app=leetcode.cn id=1689 lang=python3


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, n))


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minPartitions, ("32",), 3),
        (solution.minPartitions, ("82734",), 8),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1689 题 "十-二进制数的最少数目" 所有测试用例通过')
