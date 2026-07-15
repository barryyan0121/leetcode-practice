#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

import os
import sys
from typing import Optional

from common.node import TreeNode


# @lc code=start
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root: Optional[TreeNode]):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
            yield from leaves(root.left)
            yield from leaves(root.right)

        return list(leaves(root1)) == list(leaves(root2))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.leafSimilar,
            (
                TreeNode.create_root([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
                TreeNode.create_root(
                    [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
                ),
            ),
            True,
        ),
        (
            solution.leafSimilar,
            (TreeNode.create_root([1, 2, 3]), TreeNode.create_root([1, 3, 2])),
            False,
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
