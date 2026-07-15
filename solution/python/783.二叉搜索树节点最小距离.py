#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

import os
import sys
from typing import Optional

from common.node import TreeNode


# @lc code=start
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []
        previous = None
        answer = float("inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if previous is not None:
                answer = min(answer, root.val - previous)
            previous = root.val
            root = root.right
        return int(answer)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minDiffInBST, (TreeNode.create_root([4, 2, 6, 1, 3]),), 1),
        (
            solution.minDiffInBST,
            (TreeNode.create_root([1, 0, 48, None, None, 12, 49]),),
            1,
        ),
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
