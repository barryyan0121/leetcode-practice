#
# @lc app=leetcode.cn id=2764 lang=python3
# @lcpr version=30203
#
# [2764] 数组是否表示某二叉树的前序遍历
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        if not nodes or nodes[0][1] != -1:
            return False
        stack = [nodes[0][0]]
        children = {nodes[0][0]: 0}
        for node, parent in nodes[1:]:
            while stack and stack[-1] != parent:
                stack.pop()
            if not stack or children[stack[-1]] == 2:
                return False
            children[parent] = children.get(parent, 0) + 1
            children[node] = 0
            stack.append(node)
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPreorder([[0, -1], [1, 0], [2, 0], [3, 2], [4, 2]])
    assert not solution.isPreorder([[0, -1], [1, 0], [2, 0], [3, 1], [4, 1]])
    print("测试用例通过")
