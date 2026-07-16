#
# @lc app=leetcode.cn id=971 lang=python3
#
# [971] 翻转二叉树以匹配先序遍历
#

import os
import sys
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        position = 0
        flips = []

        def visit(node):
            nonlocal position
            if not node:
                return True
            if position == len(voyage) or node.val != voyage[position]:
                return False
            position += 1
            if (
                node.left
                and position < len(voyage)
                and node.left.val != voyage[position]
            ):
                flips.append(node.val)
                return visit(node.right) and visit(node.left)
            return visit(node.left) and visit(node.right)

        return flips if visit(root) and position == len(voyage) else [-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.flipMatchVoyage, (TreeNode.create_root([1, 2]), [2, 1]), [-1]),
        (solution.flipMatchVoyage, (TreeNode.create_root([1, 2, 3]), [1, 3, 2]), [1]),
        (solution.flipMatchVoyage, (TreeNode.create_root([1, 2, 3]), [1, 2, 3]), []),
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
