#
# @lc app=leetcode.cn id=2689 lang=python3
# @lcpr version=30203
#
# [2689] 从 Rope 树中提取第 K 个字符
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        def length(node: object) -> int:
            return len(node.val) if node.len == 0 else node.len

        while root.len:
            if root.left is None:
                root = root.right
                continue
            if root.right is None:
                root = root.left
                continue
            left_length = length(root.left)
            if k <= left_length:
                root = root.left
            else:
                k -= left_length
                root = root.right
        return root.val[k - 1]


# @lc code=end


if __name__ == "__main__":

    class RopeTreeNode:
        def __init__(self, length=0, val="", left=None, right=None):
            self.len = length
            self.val = val
            self.left = left
            self.right = right

    solution = Solution()
    root = RopeTreeNode(
        10, left=RopeTreeNode(0, "g"), right=RopeTreeNode(0, "rtaabcpoe")
    )
    assert solution.getKthCharacter(root, 6) == "b"
    assert solution.getKthCharacter(RopeTreeNode(0, "abc"), 3) == "c"
    print("测试用例通过")
