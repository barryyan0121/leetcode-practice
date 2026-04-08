#
# @lc app=leetcode.cn id=501 lang=python3
# @lcpr version=30203
#
# [501] 二叉搜索树中的众数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts: Dict[int, int] = {}

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            counts[node.val] = counts.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if not counts:
            return []

        max_count = max(counts.values())
        return sorted([val for val, cnt in counts.items() if cnt == max_count])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findMode,
            (TreeNode.create_root([1, None, 2, 2]),),
            [2],
        ),
        (
            solution.findMode,
            (TreeNode.create_root([0]),),
            [0],
        ),
        (
            solution.findMode,
            (TreeNode.create_root([1, None, 2]),),
            [1, 2],
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
# [1,null,2,2]\n
# @lcpr case=end
#
