#
# @lc app=leetcode.cn id=786 lang=python3
#
# [786] 第 K 个最小的素数分数
#

import os
import sys
from heapq import heapify, heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        last = len(arr) - 1
        heap = [(arr[index] / arr[last], index, last) for index in range(last)]
        heapify(heap)
        for _ in range(k):
            _, numerator, denominator = heappop(heap)
            if denominator - 1 > numerator:
                next_denominator = denominator - 1
                heappush(
                    heap,
                    (
                        arr[numerator] / arr[next_denominator],
                        numerator,
                        next_denominator,
                    ),
                )
        return [arr[numerator], arr[denominator]]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.kthSmallestPrimeFraction, ([1, 2, 3, 5], 3), [2, 5]),
        (solution.kthSmallestPrimeFraction, ([1, 7], 1), [1, 7]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
