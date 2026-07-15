#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        answer = 0
        start = 0
        while start + 2 < len(arr):
            end = start
            while end + 1 < len(arr) and arr[end] < arr[end + 1]:
                end += 1
            if end > start:
                peak = end
                while end + 1 < len(arr) and arr[end] > arr[end + 1]:
                    end += 1
                if end > peak:
                    answer = max(answer, end - start + 1)
            start = max(start + 1, end)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.longestMountain, ([2, 1, 4, 7, 3, 2, 5],), 5),
        (solution.longestMountain, ([2, 2, 2],), 0),
        (solution.longestMountain, ([0, 1, 0],), 3),
        (solution.longestMountain, ([0, 1, 2, 3],), 0),
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
