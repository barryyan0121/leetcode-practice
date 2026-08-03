# @lc app=leetcode.cn id=1356 lang=python3

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda value: (value.bit_count(), value))


if __name__ == "__main__":
    test_cases = [
        (
            Solution().sortByBits,
            ([0, 1, 2, 3, 4, 5, 6, 7, 8],),
            [0, 1, 2, 4, 8, 3, 5, 6, 7],
        ),
        (
            Solution().sortByBits,
            ([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],),
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1356 题 "根据数字二进制下 1 的数目排序" 所有测试用例通过')
