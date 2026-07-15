#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#

import os
import sys
from typing import List, Optional

from common.node import TreeNode


# @lc code=start
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {root: None}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if child:
                    parent[child] = node
                    stack.append(child)

        visited = {target}
        level = [target]
        for _ in range(k):
            next_level = []
            for node in level:
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        next_level.append(neighbor)
            level = next_level
        return [node.val for node in level]


# @lc code=end


if __name__ == "__main__":
    root = TreeNode.create_root([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    solution = Solution()
    test_cases = [
        (solution.distanceK, (root, root.left, 2), [7, 4, 1]),
        (solution.distanceK, (root, root, 0), [3]),
        (solution.distanceK, (root, root.right, 1), [0, 8, 3]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert sorted(result) == sorted(expected)
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
