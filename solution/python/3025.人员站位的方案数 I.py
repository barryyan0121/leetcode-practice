#
# @lc app=leetcode.cn id=3025 lang=python3
# @lcpr version=30202
#
# [3025] 人员站位的方案数 I
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                if x1 <= x2 and y1 >= y2:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if x1 <= x <= x2 and y2 <= y <= y1:
                            valid = False
                            break
                    if valid:
                        ans += 1
        return ans

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.numberOfPairs, ([[1, 1], [2, 2], [3, 3]],), 0),
        (solution.numberOfPairs, ([[6, 2], [4, 4], [2, 6]],), 2),
        (solution.numberOfPairs, ([[3, 1], [1, 3], [1, 1]],), 2),
        (solution.numberOfPairs, ([[1, 4], [2, 3], [3, 2], [4, 1]],), 3),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[6,2],[4,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,1],[1,3],[1,1]]\n
# @lcpr case=end

#
