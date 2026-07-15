#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

import os
import sys
from typing import *
from common.node import *


# @lc code=start
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        while True:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            elif node.right:
                node = node.right
            else:
                node.right = TreeNode(val)
                break
        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.insertIntoBST,
            (TreeNode.create_root([4, 2, 7, 1, 3]), 5),
            "4,2,1,null,null,3,null,null,7,5,null,null,null",
        ),
        (solution.insertIntoBST, (None, 1), "1,null,null"),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = TreeNode.print_tree(func(*args))
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
