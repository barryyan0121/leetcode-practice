#
# @lc app=leetcode.cn id=662 lang=python3
# @lcpr version=30203
#
# [662] 二叉树最大宽度
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque([(root, 0)])
        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            base = queue[0][1]
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                idx -= base
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.widthOfBinaryTree, (TreeNode.create_root([1, 3, 2, 5, 3, None, 9]),), 4),
        (solution.widthOfBinaryTree, (TreeNode.create_root([1, 3, 2, 5, None, None, 9, 6, None, 7]),), 7),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)

