#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#

import os
import sys
from typing import Optional

from common.node import TreeNode


# @lc code=start
class Solution:
    def increasingBST(self, root: TreeNode) -> Optional[TreeNode]:
        dummy = tail = TreeNode(0)
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            right = root.right
            root.left = None
            tail.right = root
            tail = root
            root = right
        return dummy.right


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.increasingBST,
            (
                TreeNode.create_root(
                    [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
                ),
            ),
            "1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9,null,null",
        ),
        (
            solution.increasingBST,
            (TreeNode.create_root([2, 1, 4, None, None, 3]),),
            "1,null,2,null,3,null,4,null,null",
        ),
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
