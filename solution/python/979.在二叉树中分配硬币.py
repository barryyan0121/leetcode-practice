#
# @lc app=leetcode.cn id=979 lang=python3
#
# [979] 在二叉树中分配硬币
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        moves = 0

        def balance(node):
            nonlocal moves
            if not node:
                return 0
            left = balance(node.left)
            right = balance(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1

        balance(root)
        return moves


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.distributeCoins, (TreeNode.create_root([3, 0, 0]),), 2),
        (solution.distributeCoins, (TreeNode.create_root([0, 3, 0]),), 3),
        (solution.distributeCoins, (TreeNode.create_root([1]),), 0),
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
