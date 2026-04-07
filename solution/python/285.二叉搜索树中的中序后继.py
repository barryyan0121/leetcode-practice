#
# @lc app=leetcode.cn id=285 lang=python3
# @lcpr version=30203
#
# [285] 二叉搜索树中的中序后继
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def inorderSuccessor(
        self, root: Optional[TreeNode], p: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root or not p:
            return None
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        succ = None
        node = root
        while node:
            if node.val > p.val:
                succ = node
                node = node.left
            else:
                node = node.right
        return succ
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    tree1 = TreeNode.create_root([2, 1, 3])
    tree2 = TreeNode.create_root([5, 3, 6, 2, 4, None, None, 1])
    test_cases = [
        (solution.inorderSuccessor, [tree1, tree1], 3),
        (solution.inorderSuccessor, [tree1, tree1.left], 2),
        (solution.inorderSuccessor, [tree2, tree2.left], 4),
        (solution.inorderSuccessor, [tree2, tree2.left.right], 5),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result_val = result.val if result else None
            assert result_val == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result_val}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result_val}"
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
# [2,1,3]\n
# @lcpr case=end

#
