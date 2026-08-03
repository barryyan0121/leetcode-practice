# @lc app=leetcode.cn id=1509 lang=python3


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        values = sorted(nums)
        return (
            min(values[index + len(values) - 4] - values[index] for index in range(4))
            if len(values) > 4
            else 0
        )


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minDifference, ([5, 3, 2, 4],), 0),
        (solution.minDifference, ([1, 5, 0, 10, 14],), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1509 题 "三次操作后最大值与最小值的最小差" 所有测试用例通过')
