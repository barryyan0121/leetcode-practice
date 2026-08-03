# @lc app=leetcode.cn id=1503 lang=python3


class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        return max([*left, *(n - position for position in right)], default=0)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.getLastMoment, (4, [4, 3], [0, 1]), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1503 题 "所有蚂蚁掉下来前的最后一刻" 所有测试用例通过')
