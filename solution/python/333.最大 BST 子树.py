#
# @lc app=leetcode.cn id=333 lang=python3
# @lcpr version=30203
#
# [333] 最大 BST 子树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int, int, int, int]:
            if not node:
                return True, 0, float("inf"), float("-inf"), 0

            left_bst, left_size, left_min, left_max, left_best = dfs(node.left)
            right_bst, right_size, right_min, right_max, right_best = dfs(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                return True, size, min(left_min, node.val), max(right_max, node.val), size
            return False, 0, 0, 0, max(left_best, right_best)

        return dfs(root)[4]
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.largestBSTSubtree, [TreeNode.create_root([10, 5, 15, 1, 8, None, 7])], 3),
        (solution.largestBSTSubtree, [TreeNode.create_root([2, 1, 3])], 3),
        (solution.largestBSTSubtree, [TreeNode.create_root([])], 0),
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
# [10,5,15,1,8,null,7]\n
# @lcpr case=end

#
