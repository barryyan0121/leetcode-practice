#
# @lc app=leetcode.cn id=549 lang=python3
# @lcpr version=30203
#
# [549] 二叉树最长连续序列 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal best
            if not node:
                return 0, 0
            inc = dec = 1
            if node.left:
                l_inc, l_dec = dfs(node.left)
                if node.left.val == node.val + 1:
                    inc = max(inc, l_inc + 1)
                if node.left.val == node.val - 1:
                    dec = max(dec, l_dec + 1)
            if node.right:
                r_inc, r_dec = dfs(node.right)
                if node.right.val == node.val + 1:
                    inc = max(inc, r_inc + 1)
                if node.right.val == node.val - 1:
                    dec = max(dec, r_dec + 1)
            best = max(best, inc + dec - 1)
            return inc, dec

        dfs(root)
        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.longestConsecutive,
            (TreeNode.create_root([1, 2, 3]),),
            2,
        ),
        (
            solution.longestConsecutive,
            (TreeNode.create_root([2, 1, 3]),),
            3,
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
# [1,2,3]\n
# @lcpr case=end
#
