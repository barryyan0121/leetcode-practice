#
# @lc app=leetcode.cn id=270 lang=python3
# @lcpr version=30203
#
# [270] 最接近的二叉搜索树值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        current = root

        while current is not None:
            if abs(current.val - target) < abs(closest - target):
                closest = current.val
            if target < current.val:
                current = current.left
            else:
                current = current.right

        return closest


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.closestValue, (TreeNode.create_root([4, 2, 5, 1, 3]), 3.714286), 4),
        (solution.closestValue, (TreeNode.create_root([1]), 4.428571), 1),
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
# [4,2,5,1,3]\n3.714286\n
# @lcpr case=end
