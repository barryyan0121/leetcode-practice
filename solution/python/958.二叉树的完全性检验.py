#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#

import os
import sys
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        missing = False
        while queue:
            node = queue.popleft()
            if not node:
                missing = True
            elif missing:
                return False
            else:
                queue.append(node.left)
                queue.append(node.right)
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isCompleteTree, (TreeNode.create_root([1, 2, 3, 4, 5, 6]),), True),
        (
            solution.isCompleteTree,
            (TreeNode.create_root([1, 2, 3, 4, 5, None, 7]),),
            False,
        ),
        (solution.isCompleteTree, (TreeNode.create_root([1]),), True),
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
