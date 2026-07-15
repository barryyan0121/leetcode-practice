#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal longest
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            left_path = left + 1 if node.left and node.left.val == node.val else 0
            right_path = right + 1 if node.right and node.right.val == node.val else 0
            longest = max(longest, left_path + right_path)
            return max(left_path, right_path)

        dfs(root)
        return longest


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.longestUnivaluePath,
            (TreeNode.create_root([5, 4, 5, 1, 1, None, 5]),),
            2,
        ),
        (
            solution.longestUnivaluePath,
            (TreeNode.create_root([1, 4, 5, 4, 4, None, 5]),),
            2,
        ),
        (solution.longestUnivaluePath, (None,), 0),
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
