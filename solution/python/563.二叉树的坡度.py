#
# @lc app=leetcode.cn id=563 lang=python3
# @lcpr version=30203
#
# [563] 二叉树的坡度
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal total
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            total += abs(left - right)
            return left + right + node.val

        dfs(root)
        return total


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findTilt, (TreeNode.create_root([1, 2, 3]),), 1),
        (
            solution.findTilt,
            (TreeNode.create_root([4, 2, 9, 3, 5, None, 7]),),
            15,
        ),
        (solution.findTilt, (TreeNode.create_root([1]),), 0),
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
# [1,2,3]\n
# @lcpr case=end
#
