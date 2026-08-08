# @lc app=leetcode.cn id=1426 lang=python3

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        values = set(arr)
        return sum(value + 1 in values for value in arr)


if __name__ == "__main__":
    test_cases = [
        (Solution().countElements, ([1, 2, 3],), 2),
        (Solution().countElements, ([1, 1, 3, 3, 5, 5, 7, 7],), 0),
        (Solution().countElements, ([1, 1, 2],), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1426 题 "数元素" 所有测试用例通过')
