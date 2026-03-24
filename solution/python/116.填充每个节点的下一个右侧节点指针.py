#
# @lc app=leetcode.cn id=116 lang=python3
# @lcpr version=30203
#
# [116] 填充每个节点的下一个右侧节点指针
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# @lc code=start
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_perfect_tree(values: List[Optional[int]]) -> Optional[Node]:
        if not values:
            return None
        nodes = [Node(v) if v is not None else None for v in values]
        for i, node in enumerate(nodes):
            if not node:
                continue
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
        return nodes[0]

    def levels_with_next(root: Optional[Node]) -> List[List[int]]:
        res = []
        level = root
        while level:
            cur = level
            row = []
            while cur:
                row.append(cur.val)
                cur = cur.next
            res.append(row)
            level = level.left
        return res

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.connect,
            [build_perfect_tree([1, 2, 3, 4, 5, 6, 7])],
            [[1], [2, 3], [4, 5, 6, 7]],
        ),
        (solution.connect, [build_perfect_tree([1])], [[1]]),
        (solution.connect, [None], []),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            if args[0] is None:
                result = []
            else:
                result = levels_with_next(args[0])
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
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
