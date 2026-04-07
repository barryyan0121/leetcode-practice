#
# @lc app=leetcode.cn id=406 lang=python3
# @lcpr version=30203
#
# [406] 根据身高重建队列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.reconstructQueue,
            [[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]],
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        ),
        (
            solution.reconstructQueue,
            [[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]],
            [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]],
        ),
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
# [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]\n
# @lcpr case=end

#
