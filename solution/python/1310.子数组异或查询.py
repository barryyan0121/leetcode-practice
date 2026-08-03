# @lc app=leetcode.cn id=1310 lang=python3

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for value in arr:
            prefix.append(prefix[-1] ^ value)
        return [prefix[right + 1] ^ prefix[left] for left, right in queries]


if __name__ == "__main__":
    test_cases = [
        (
            Solution().xorQueries,
            ([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]),
            [2, 7, 14, 8],
        ),
        (
            Solution().xorQueries,
            ([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]),
            [8, 0, 4, 4],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1310 题 "子数组异或查询" 所有测试用例通过')
