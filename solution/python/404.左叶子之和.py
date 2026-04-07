#
# @lc app=leetcode.cn id=404 lang=python3
# @lcpr version=30203
#
# [404] 左叶子之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val
        return ans + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = [root]
        idx = 1
        for node in queue:
            if idx >= len(values):
                break
            left_val = values[idx]
            idx += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            if idx >= len(values):
                break
            right_val = values[idx]
            idx += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        return root

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.sumOfLeftLeaves, [build_tree([3, 9, 20, None, None, 15, 7])], 24),
        (solution.sumOfLeftLeaves, [build_tree([1])], 0),
        (solution.sumOfLeftLeaves, [None], 0),
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
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

#
