#
# @lc app=leetcode.cn id=95 lang=python3
# @lcpr version=30202
#
# [95] 不同的二叉搜索树 II
#

import sys
import os
from functools import lru_cache

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        @lru_cache(None)
        def build(lo: int, hi: int) -> Tuple[Optional[TreeNode], ...]:
            if lo > hi:
                return (None,)

            trees = []
            for root_val in range(lo, hi + 1):
                for left in build(lo, root_val - 1):
                    for right in build(root_val + 1, hi):
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return tuple(trees)

        return list(build(1, n))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def serialize(root: Optional[TreeNode]) -> List[Optional[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        for node in queue:
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.generateTrees,
            [3],
            [
                [1, None, 2, None, 3],
                [1, None, 3, 2],
                [2, 1, 3],
                [3, 1, None, None, 2],
                [3, 2, None, 1],
            ],
        ),
        (solution.generateTrees, [1], [[1]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = [serialize(tree) for tree in func(*args)]
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
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
