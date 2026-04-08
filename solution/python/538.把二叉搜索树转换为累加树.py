#
# @lc app=leetcode.cn id=538 lang=python3
# @lcpr version=30203
#
# [538] 把二叉搜索树转换为累加树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal total
            if node is None:
                return
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)

        dfs(root)
        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.convertBST,
            (
                TreeNode.create_root(
                    [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
                ),
            ),
            "30,36,36,null,null,35,null,33,null,null,21,26,null,null,15,null,8,null,null",
        ),
        (
            solution.convertBST,
            (TreeNode.create_root([0, None, 1]),),
            "1,null,1,null,null",
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            printed = TreeNode.print_tree(result)
            assert printed == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {printed}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {printed}"
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
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
# @lcpr case=end
#
