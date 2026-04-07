#
# @lc app=leetcode.cn id=272 lang=python3
# @lcpr version=30203
#
# [272] 最接近的二叉搜索树值 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def closestKValues(
        self, root: Optional[TreeNode], target: float, k: int
    ) -> List[int]:
        values = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        left = 0
        while len(values) - left > k:
            if abs(values[left] - target) <= abs(values[-1] - target):
                values.pop()
            else:
                left += 1
        return values[left:]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.closestKValues,
            (TreeNode.create_root([4, 2, 5, 1, 3]), 3.714286, 2),
            [3, 4],
        ),
        (
            solution.closestKValues,
            (TreeNode.create_root([4, 2, 5, 1, 3]), 3.0, 3),
            [2, 3, 4],
        ),
        (
            solution.closestKValues,
            (TreeNode.create_root([1]), 0.0, 1),
            [1],
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
# [4,2,5,1,3]\n3.714286\n2\n
# @lcpr case=end
