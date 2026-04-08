#
# @lc app=leetcode.cn id=559 lang=python3
# @lcpr version=30203
#
# [559] N 叉树的最大深度
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children if children is not None else []


# @lc code=start
class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        return 1 + max((self.maxDepth(child) for child in root.children), default=0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    test_cases = [
        (solution.maxDepth, (root,), 3),
        (solution.maxDepth, (None,), 0),
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
# [1,[3,[5,6],2,4]]\n
# @lcpr case=end
#
