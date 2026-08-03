# @lc app=leetcode.cn id=1385 lang=python3
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ordered = sorted(arr2)
        return sum(
            bisect_left(ordered, value - d) == bisect_right(ordered, value + d)
            for value in arr1
        )


if __name__ == "__main__":
    test_cases = [
        (Solution().findTheDistanceValue, ([4, 5, 8], [10, 9, 1, 8], 2), 2),
        (
            Solution().findTheDistanceValue,
            ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3),
            2,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1385 题 "两个数组间的距离值" 所有测试用例通过')
