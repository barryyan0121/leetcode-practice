#
# @lc app=leetcode.cn id=145 lang=python3
# @lcpr version=30202
#
# [145] 二叉树的后序遍历
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.postorderTraversal,
            (TreeNode.create_root([1, None, 2, 3]),),
            [3, 2, 1],
        ),
        (solution.postorderTraversal, (TreeNode.create_root([]),), []),
        (solution.postorderTraversal, (TreeNode.create_root([1]),), [1]),
        (
            solution.postorderTraversal,
            (TreeNode.create_root([1, 2, 3, 4, 5]),),
            [4, 5, 2, 3, 1],
        ),
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
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
