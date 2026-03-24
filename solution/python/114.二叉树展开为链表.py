#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30203
#
# [114] 二叉树展开为链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
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

    def to_right_chain(root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            res.append(root.val)
            assert root.left is None
            root = root.right
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.flatten,
            [build_tree([1, 2, 5, 3, 4, None, 6])],
            [1, 2, 3, 4, 5, 6],
        ),
        (solution.flatten, [build_tree([])], []),
        (solution.flatten, [build_tree([0])], [0]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            if args[0] is None:
                result = []
            else:
                result = to_right_chain(args[0])
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
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
