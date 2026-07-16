#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        cameras = 0

        def visit(node):
            nonlocal cameras
            if not node:
                return 1
            left, right = visit(node.left), visit(node.right)
            if left == 0 or right == 0:
                cameras += 1
                return 2
            if left == 2 or right == 2:
                return 1
            return 0

        if visit(root) == 0:
            cameras += 1
        return cameras


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minCameraCover, (TreeNode.create_root([0, 0, None, 0, 0]),), 1),
        (
            solution.minCameraCover,
            (TreeNode.create_root([0, 0, None, 0, None, 0, None, None, 0]),),
            2,
        ),
        (solution.minCameraCover, (TreeNode.create_root([0]),), 1),
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
