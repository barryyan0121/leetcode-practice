#
# @lc app=leetcode.cn id=103 lang=python3
# @lcpr version=30202
#
# [103] 二叉树的锯齿形层序遍历
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = [root]
        left_to_right = True

        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            queue = next_queue
            left_to_right = not left_to_right

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.zigzagLevelOrder,
            (TreeNode.create_root([3, 9, 20, None, None, 15, 7]),),
            [[3], [20, 9], [15, 7]],
        ),
        (
            solution.zigzagLevelOrder,
            (TreeNode.create_root([1, 2, 3, 4, None, None, 5]),),
            [[1], [3, 2], [4, 5]],
        ),
        (solution.zigzagLevelOrder, (None,), []),
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
