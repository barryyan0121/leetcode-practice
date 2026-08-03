# @lc app=leetcode.cn id=1388 lang=python3
from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        choose = len(slices) // 3

        def solve(values):
            before_previous = [0] * (choose + 1)
            previous = [0] * (choose + 1)
            for value in values:
                current = previous[:]
                for count in range(1, choose + 1):
                    current[count] = max(
                        current[count], before_previous[count - 1] + value
                    )
                before_previous, previous = previous, current
            return previous[choose]

        return max(solve(slices[1:]), solve(slices[:-1]))


if __name__ == "__main__":
    test_cases = [
        (Solution().maxSizeSlices, ([1, 2, 3, 4, 5, 6],), 10),
        (Solution().maxSizeSlices, ([8, 9, 8, 6, 1, 1],), 16),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1388 题 "3n 块披萨" 所有测试用例通过')
