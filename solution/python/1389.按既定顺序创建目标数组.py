# @lc app=leetcode.cn id=1389 lang=python3
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for value, position in zip(nums, index):
            result.insert(position, value)
        return result


if __name__ == "__main__":
    test_cases = [
        (
            Solution().createTargetArray,
            ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]),
            [0, 4, 1, 3, 2],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1389 题 "按既定顺序创建目标数组" 所有测试用例通过')
