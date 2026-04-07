#
# @lc app=leetcode.cn id=254 lang=python3
# @lcpr version=30203
#
# [254] 因子的组合
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int, remain: int) -> None:
            if remain == 1:
                if len(path) > 1:
                    res.append(path[:])
                return
            for f in range(start, int(remain ** 0.5) + 1):
                if remain % f == 0:
                    path.append(f)
                    dfs(f, remain // f)
                    path.pop()
            if remain >= start and remain != n:
                path.append(remain)
                res.append(path[:])
                path.pop()

        dfs(2, n)
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.getFactors, [12], [[2, 2, 3], [2, 6], [3, 4]]),
        (solution.getFactors, [37], []),
        (solution.getFactors, [32], [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 2, 8], [2, 4, 4], [2, 16], [4, 8]]),
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
# 12\n
# @lcpr case=end

#
