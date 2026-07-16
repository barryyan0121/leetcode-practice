#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if low <= node.val <= high:
                total += node.val
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
        return total


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.rangeSumBST,
            (TreeNode.create_root([10, 5, 15, 3, 7, None, 18]), 7, 15),
            32,
        ),
        (
            solution.rangeSumBST,
            (TreeNode.create_root([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10),
            23,
        ),
        (solution.rangeSumBST, (TreeNode.create_root([1]), 1, 1), 1),
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
