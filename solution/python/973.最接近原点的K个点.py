#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda point: point[0] ** 2 + point[1] ** 2)[:k]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.kClosest, ([[1, 3], [-2, 2]], 1), [[-2, 2]]),
        (solution.kClosest, ([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]]),
        (solution.kClosest, ([[0, 1]], 1), [[0, 1]]),
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
