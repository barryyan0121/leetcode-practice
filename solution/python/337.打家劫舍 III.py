#
# @lc app=leetcode.cn id=337 lang=python3
# @lcpr version=30203
#
# [337] 打家劫舍 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            rob_cur = node.val + left[1] + right[1]
            skip_cur = max(left) + max(right)
            return rob_cur, skip_cur

        return max(dfs(root))
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.rob, [TreeNode.create_root([3, 2, 3, None, 3, None, 1])], 7),
        (solution.rob, [TreeNode.create_root([3, 4, 5, 1, 3, None, 1])], 9),
        (solution.rob, [TreeNode.create_root([])], 0),
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
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

#
