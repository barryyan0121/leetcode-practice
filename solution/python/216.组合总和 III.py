#
# @lc app=leetcode.cn id=216 lang=python3
# @lcpr version=30203
#
# [216] 组合总和 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int, remain_k: int, remain_n: int) -> None:
            if remain_k == 0:
                if remain_n == 0:
                    res.append(path[:])
                return
            for num in range(start, 10):
                if num > remain_n:
                    break
                path.append(num)
                dfs(num + 1, remain_k - 1, remain_n - num)
                path.pop()

        dfs(1, k, n)
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.combinationSum3, [3, 7], [[1, 2, 4]]),
        (solution.combinationSum3, [3, 9], [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        (solution.combinationSum3, [4, 1], []),
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
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n9\n
# @lcpr case=end

#
