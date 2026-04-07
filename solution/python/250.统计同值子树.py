#
# @lc app=leetcode.cn id=250 lang=python3
# @lcpr version=30203
#
# [250] 统计同值子树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            nonlocal ans
            if not node:
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            if not left or not right:
                return False
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            ans += 1
            return True

        dfs(root)
        return ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.countUnivalSubtrees,
            [TreeNode.create_root([5, 1, 5, 5, 5, None, 5])],
            4,
        ),
        (
            solution.countUnivalSubtrees,
            [TreeNode.create_root([1, 1, 1, 1, 1, None, 1])],
            6,
        ),
        (solution.countUnivalSubtrees, [TreeNode.create_root([])], 0),
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
# [5,1,5,5,5,null,5]\n
# @lcpr case=end

#
