#
# @lc app=leetcode.cn id=117 lang=python3
# @lcpr version=30203
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# @lc code=start
class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return None

        queue = [root]
        while queue:
            next_queue = []
            prev = None
            for node in queue:
                if prev is not None:
                    prev.next = node
                prev = node
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue

        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_tree(values: List[Optional[int]]) -> Optional[Node]:
        if not values or values[0] is None:
            return None
        root = Node(values[0])
        queue = [root]
        idx = 1
        for node in queue:
            if idx >= len(values):
                break
            left_val = values[idx]
            idx += 1
            if left_val is not None:
                node.left = Node(left_val)
                queue.append(node.left)
            if idx >= len(values):
                break
            right_val = values[idx]
            idx += 1
            if right_val is not None:
                node.right = Node(right_val)
                queue.append(node.right)
        return root

    def serialize_next_levels(root: Optional[Node]) -> List[List[int]]:
        result = []
        level_start = root
        while level_start:
            level = []
            curr = level_start
            next_start = None
            while curr:
                level.append(curr.val)
                if next_start is None:
                    next_start = curr.left or curr.right
                curr = curr.next
            result.append(level)
            level_start = next_start
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.connect,
            (build_tree([1, 2, 3, 4, 5, None, 7]),),
            [[1], [2, 3], [4, 5, 7]],
        ),
        (
            solution.connect,
            (build_tree([1, 2, 3, 4, None, None, 5]),),
            [[1], [2, 3], [4, 5]],
        ),
        (solution.connect, (None,), []),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result = serialize_next_levels(result) if result else []
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
# [1,2,3,4,5,null,7]\n
# @lcpr case=end
