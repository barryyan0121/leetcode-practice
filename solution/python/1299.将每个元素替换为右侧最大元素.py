# @lc app=leetcode.cn id=1299 lang=python3

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        for index in range(len(arr) - 1, -1, -1):
            arr[index], maximum = maximum, max(maximum, arr[index])
        return arr


if __name__ == "__main__":
    test_cases = [
        (Solution().replaceElements, ([17, 18, 5, 4, 6, 1],), [18, 6, 6, 6, 1, -1]),
        (Solution().replaceElements, ([400],), [-1]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1299 题 "将每个元素替换为右侧最大元素" 所有测试用例通过')
