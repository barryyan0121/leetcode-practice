# @lc app=leetcode.cn id=1313 lang=python3

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [
            value
            for frequency, value in zip(nums[::2], nums[1::2])
            for _ in range(frequency)
        ]


if __name__ == "__main__":
    test_cases = [
        (Solution().decompressRLElist, ([1, 2, 3, 4],), [2, 4, 4, 4]),
        (Solution().decompressRLElist, ([1, 1, 1, 2],), [1, 2]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1313 题 "解压缩编码列表" 所有测试用例通过')
