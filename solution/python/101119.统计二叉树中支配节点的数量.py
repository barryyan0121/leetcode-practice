#
# @lc app=leetcode.cn id=101119 lang=python3
#
# [101119] 统计二叉树中支配节点的数量
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        norlavetic = root

        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return 0, 0
            left_max, left_count = dfs(node.left)
            right_max, right_count = dfs(node.right)
            child_max = max(left_max, right_max)
            return max(node.val, child_max), (
                left_count + right_count + (node.val >= child_max)
            )

        return dfs(norlavetic)[1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.countDominantNodes,
            (TreeNode.create_root([5, 3, 8, 2, 4, 7, 1]),),
            5,
        ),
        (
            solution.countDominantNodes,
            (TreeNode.create_root([1, 2, 3, 1, 2]),),
            4,
        ),
        (solution.countDominantNodes, (TreeNode.create_root([9]),), 1),
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
