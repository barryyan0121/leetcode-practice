#
# @lc app=leetcode.cn id=558 lang=python3
# @lcpr version=30203
#
# [558] 四叉树交集
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Optional["Node"] = None,
        topRight: Optional["Node"] = None,
        bottomLeft: Optional["Node"] = None,
        bottomRight: Optional["Node"] = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# @lc code=start
class Solution:
    def intersect(self, quadTree1: "Node", quadTree2: "Node") -> "Node":
        if quadTree1.isLeaf:
            return Node(True, True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return Node(True, True) if quadTree2.val else quadTree1

        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        children = [topLeft, topRight, bottomLeft, bottomRight]
        if all(child.isLeaf and child.val == children[0].val for child in children):
            return Node(children[0].val, True)
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_left() -> Node:
        return Node(
            False,
            False,
            Node(True, True),
            Node(False, True),
            Node(False, True),
            Node(False, True),
        )

    def build_right() -> Node:
        return Node(True, True)

    def count_nodes(node: Optional[Node]) -> int:
        if not node:
            return 0
        if node.isLeaf:
            return 1
        return 1 + sum(
            count_nodes(child)
            for child in [
                node.topLeft,
                node.topRight,
                node.bottomLeft,
                node.bottomRight,
            ]
        )

    test_cases = [
        (count_nodes, (solution.intersect(build_left(), build_right()),), 1),
        (count_nodes, (solution.intersect(build_right(), build_left()),), 1),
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
# quadTree1 = [[0,1],[1,0]], quadTree2 = [[1,1],[1,1]]\n
# @lcpr case=end
#
