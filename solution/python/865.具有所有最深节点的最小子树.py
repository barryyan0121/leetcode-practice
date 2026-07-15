#
# @lc app=leetcode.cn id=865 lang=python3
#
# [865] 具有所有最深节点的最小子树
#

import os
import sys
from typing import Optional, Tuple

from common.node import TreeNode


# @lc code=start
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def search(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            if not node:
                return None, 0
            left_node, left_depth = search(node.left)
            right_node, right_depth = search(node.right)
            if left_depth == right_depth:
                return node, left_depth + 1
            if left_depth > right_depth:
                return left_node, left_depth + 1
            return right_node, right_depth + 1

        return search(root)[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    roots = [
        TreeNode.create_root([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
        TreeNode.create_root([1]),
        TreeNode.create_root([0, 1, 3, None, 2]),
    ]
    test_cases = [
        (solution.subtreeWithAllDeepest, (roots[0],), 2),
        (solution.subtreeWithAllDeepest, (roots[1],), 1),
        (solution.subtreeWithAllDeepest, (roots[2],), 2),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args).val
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
