# @lc app=leetcode.cn id=1343 lang=python3

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window = sum(arr[:k])
        result = int(window >= target)
        for index in range(k, len(arr)):
            window += arr[index] - arr[index - k]
            result += window >= target
        return result


if __name__ == "__main__":
    test_cases = [
        (Solution().numOfSubarrays, ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4), 3),
        (Solution().numOfSubarrays, ([1, 1, 1, 1, 1], 1, 0), 5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1343 题 "大小为 K 且平均值大于等于阈值的子数组数目" 所有测试用例通过')
