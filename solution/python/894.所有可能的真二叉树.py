#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的真二叉树
#

import os
import sys
from functools import cache
from typing import List

from common.node import TreeNode


# @lc code=start
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n == 1:
            return [TreeNode(0)]
        trees = []
        for left_size in range(1, n, 2):
            for left in self.allPossibleFBT(left_size):
                for right in self.allPossibleFBT(n - left_size - 1):
                    root = TreeNode(0)
                    root.left, root.right = left, right
                    trees.append(root)
        return trees


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.allPossibleFBT, (7,), 5),
        (solution.allPossibleFBT, (3,), 1),
        (solution.allPossibleFBT, (2,), 0),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = len(func(*args))
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
