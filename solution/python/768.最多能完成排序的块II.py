#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        suffix_minimum = arr[:]
        for index in range(len(arr) - 2, -1, -1):
            suffix_minimum[index] = min(
                suffix_minimum[index], suffix_minimum[index + 1]
            )

        chunks = 1
        prefix_maximum = arr[0]
        for index in range(len(arr) - 1):
            prefix_maximum = max(prefix_maximum, arr[index])
            chunks += prefix_maximum <= suffix_minimum[index + 1]
        return chunks


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxChunksToSorted, ([5, 4, 3, 2, 1],), 1),
        (solution.maxChunksToSorted, ([2, 1, 3, 4, 4],), 4),
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
