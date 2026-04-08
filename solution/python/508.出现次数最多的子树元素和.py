#
# @lc app=leetcode.cn id=508 lang=python3
# @lcpr version=30203
#
# [508] 出现次数最多的子树元素和
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        counts = Counter()

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            subtotal = node.val + dfs(node.left) + dfs(node.right)
            counts[subtotal] += 1
            return subtotal

        dfs(root)
        best = max(counts.values())
        return [subtotal for subtotal, freq in counts.items() if freq == best]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.findFrequentTreeSum,
            (TreeNode.create_root([5, 2, -3]),),
            [-3, 2, 4],
        ),
        (
            solution.findFrequentTreeSum,
            (TreeNode.create_root([5, 2, -5]),),
            [2],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = sorted(func(*args))
            assert result == sorted(expected)
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {sorted(expected)}, 实际 = {result}"
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
# [5,2,-5]\n
# @lcpr case=end
#
