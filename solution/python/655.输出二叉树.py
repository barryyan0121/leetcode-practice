#
# @lc app=leetcode.cn id=655 lang=python3
# @lcpr version=30203
#
# [655] 输出二叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node: Optional[TreeNode]) -> int:
            return 0 if not node else 1 + max(height(node.left), height(node.right))

        h = height(root)
        ans = [[""] * (2**h - 1) for _ in range(h)]

        def fill(node: Optional[TreeNode], row: int, left: int, right: int) -> None:
            if not node:
                return
            mid = (left + right) // 2
            ans[row][mid] = str(node.val)
            fill(node.left, row + 1, left, mid - 1)
            fill(node.right, row + 1, mid + 1, right)

        fill(root, 0, 0, len(ans[0]) - 1)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.printTree, (TreeNode.create_root([1, 2]),), [["", "1", ""], ["2", "", ""]]),
        (solution.printTree, (TreeNode.create_root([1, 2, 3, None, 4]),), [["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)

